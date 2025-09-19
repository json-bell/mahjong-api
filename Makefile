# Start the FastAPI server
start:
	uvicorn app.main:app --reload
	
# Run tests - TODO
test:
	echo "No test system defined"

# Freeze requirements
freeze:
	pip freeze > requirements.txt


# Activate venv
venv:
	source venv/bin/activate