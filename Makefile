# Variables
PYTHON := venv/bin/python
PIP := venv/bin/pip
UVICORN := venv/bin/uvicorn

# Start the FastAPI server
start:
	$(UVICORN) app.main:app --reload

# Run tests - TODO
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
	flake8 .
	mypy .