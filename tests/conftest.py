import os
import pytest


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
