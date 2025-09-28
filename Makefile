# ------------------------
# Variables
# ------------------------
PYTHON := venv/bin/python
PIP := venv/bin/pip
UVICORN := venv/bin/uvicorn

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
	$(PIP) install --upgrade pip wheel

install: venv ## Install project dependencies
	$(PIP) install -r requirements.txt

install-precommit: ## Setup pre-commit hooks
	@echo "Installing pre-commit hooks..."
	pre-commit install
	pre-commit install --hook-type pre-push

# ------------------------
# Database
# ------------------------
setup-dbs:
	psql -f ./app/db/setup_dbs.sql

# TODO
seed: @echo "Seeding not yet set up"

# ------------------------
# Run & test
# ------------------------
start: ## Start FastAPI server
	@echo "Starting FastAPI in $(ENV) environment..."
	$(UVICORN) app.main:app --reload

test: ## Run tests (always uses test environment)
	ENV=test $(PYTHON) -m pytest

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
	$(PIP) freeze > requirements.txt
