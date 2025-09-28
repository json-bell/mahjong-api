import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Annotated


# Determine which environment to use (default to dev)
ENV = os.getenv("ENV", "dev")  # 'dev', 'test', or 'prod'

# Load the corresponding .env file
env_path = Path(f".env.{ENV}")
if not env_path.exists():
    raise FileNotFoundError(f"{env_path} not found! Make sure your .env files exist.")

load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):  # type: ignore[valid-type] # type:ignore[misc]
    database_url: Annotated[str, Field(..., env="DATABASE_URL")]

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
    )


settings = Settings()
if not settings.database_url:
    raise RuntimeError("DATABASE_URL is missing from your environment")

# Stop if tests are not in test environment
if ENV == "test" and "test" not in settings.database_url:
    raise RuntimeError(
        f"ENV=test but DATABASE_URL does not point to test DB! Current: {settings.database_url}"
    )
