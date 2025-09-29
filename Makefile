# Default environment
ENV ?= dev

# ------------------------
# Phony targets
# ------------------------
.PHONY: start seed-dbs test freeze install venv install-precommit check lint

# ------------------------
# Virtual environment & dependencies
# ------------------------
venv: ## Create virtual environment
	python3 -m venv venv
	pip install --upgrade pip wheel

install: venv ## Install project dependencies
	pip install -r requirements.txt

install-precommit: ## Setup pre-commit hooks
	@echo "Installing pre-commit hooks..."
	pre-commit install
	pre-commit install --hook-type pre-push

# ------------------------
# Database
# ------------------------
setup-dbs:
	psql -f ./app/db/setup_dbs.sql

seed:
	python -m scripts.seed

# Alembic commands
migrate:
ifeq ($(MSG),)
	$(error MSG is not set. Usage: make migrate MSG="your message" [ENV=dev|prod])
endif
	@echo "Creating new migration for $(ENV) with message: $(MSG)"
	alembic revision --autogenerate -m "$(MSG)"

upgrade:
	@echo "Upgrading database for $(ENV)..."
	alembic upgrade head

downgrade:
	@echo "Downgrading last migration for $(ENV)..."
	alembic downgrade -1

history:
	@echo "Showing migration history for $(ENV)..."
	alembic history --verbose

# ------------------------
# Run & test
# ------------------------
start: ## Start FastAPI server
	@echo "Starting FastAPI in $(ENV) environment..."
	uvicorn app.main:app --reload

test: ## Run tests (always uses test environment)
	ENV=test python -m pytest

# ------------------------
# Code quality
# ------------------------
check: ## Run pre-commit checks
	pre-commit run --all-files

lint: ## Run linters
	flake8 app tests
	mypy app tests

# ------------------------
# Utilities
# ------------------------
freeze: ## Freeze requirements
	pip freeze > requirements.txt
