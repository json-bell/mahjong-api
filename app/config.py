import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


# Determine which environment to use (default to dev)
ENV = os.getenv("ENV", "dev")  # 'dev', 'test', or 'prod'

# Load the corresponding .env file
env_path = Path(f".env.{ENV}")
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    print(f"[INFO] Loaded environment variables from {env_path}")

else:
    if ENV == "prod":
        print(
            "[INFO] Production environment detected, loading system environment variables."
        )
    else:
        print(
            f"[WARNING] {env_path} not found. Falling back to system environment variables."
        )


class Settings(BaseSettings):
    internal_database_url: str | None = Field(default=None, alias="DATABASE_URL")
    pgdatabase: str | None = Field(default=None, alias="PGDATABASE")

    # Optional Postgres parts with defaults
    pguser: str = Field(default="postgres", alias="PGUSER")
    pgpassword: str | None = Field(default=None, alias="PGPASSWORD")
    pghost: str = Field(default="localhost", alias="PGHOST")
    pgport: str = Field(default="5432", alias="PGPORT")

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
    )

    @property
    def env(self) -> str:
        return ENV

    @property
    def database_url(self) -> str:
        if settings.internal_database_url:
            return settings.internal_database_url

        if not settings.pgdatabase:
            raise RuntimeError(
                "Neither DATABASE_URL nor PGDATABASE found in environment"
            )

        else:
            password = f":{self.pgpassword}" if self.pgpassword else ""
        return f"postgresql://{self.pguser}{password}@{self.pghost}:{self.pgport}/{self.pgdatabase}"


settings = Settings()
if not settings.database_url:
    raise RuntimeError("DATABASE_URL is missing from your environment")

# Stop if tests are not in test environment
if ENV == "test" and "test" not in settings.database_url:
    raise RuntimeError(
        f"ENV=test but DATABASE_URL does not point to test DB - current: {settings.database_url}"
    )
