# Variables
PYTHON := venv/bin/python
PIP := venv/bin/pip
UVICORN := venv/bin/uvicorn

# Default environment
ENV ?= dev

# Paths to .env files
ENV_FILE := .env.$(ENV)

# Export ENV so subprocesses know which environment is active
export ENV

# Load .env file before running commands
define load_env
	@echo "Loading environment $(ENV) from $(ENV_FILE)"
	@export $(shell sed 's/=.*//' $(ENV_FILE))
endef

# Start the FastAPI server
start:
	@echo "Starting FastAPI in $(ENV) environment..."
	@export ENV=$(ENV) && $(UVICORN) app.main:app --reload

# Run tests
test:
	$(PYTHON) -m pytest

# Freeze requirements
freeze:
	$(PIP) freeze > requirements.txt


install: venv # Install dependencies
	$(PIP) install -r requirements.txt

# Create venv if it doesn't exist
venv: ## Create virtual environment
	python3 -m venv venv
	$(PIP) install --upgrade pip wheel

# Sets up pre-commit hooks and pushes
install-precommit:
	@echo "Installing pre-commit hooks..."
	pre-commit install          # pre-commit hook
	pre-commit install --hook-type pre-push  # pre-push hook

check:
	pre-commit run --all-files

lint:
	flake8 app tests
	mypy app tests