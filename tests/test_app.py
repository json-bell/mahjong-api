from fastapi.testclient import TestClient
from app.main import app  # your FastAPI app
import json

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_endpoints():
    response = client.get("/api")
    assert response.status_code == 200
    data = response.json()
    with open("app/endpoints.json") as f:
        expected_data = json.load(f)
    assert data == expected_data
