import os
import pytest
from fastapi.testclient import TestClient
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.main import app  # your FastAPI app
from app.db.models import Game
from app.db.dependencies import get_db


def pytest_sessionstart(session):
    """
    Abort the entire test session if ENV is not set to 'test'.
    """
    env = os.getenv("ENV")
    if env is None:
        pytest.exit("❌ ENV not set. Did you mean to run with ENV=test?")
    if env != "test":
        pytest.exit(
            f"❌ Refusing to run tests with ENV={env!r}. "
            "Set ENV=test before running pytest."
        )


@pytest.fixture(scope="session")
def db_engine():
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session(db_engine):
    """Create a transactional session for each test."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db_session):
    def _get_test_db():
        yield db_session

    app.dependency_overrides[get_db] = _get_test_db
    yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def seed_data(db_session):
    game = Game()
    db_session.add(game)
    db_session.commit()
    return {"game": game}
