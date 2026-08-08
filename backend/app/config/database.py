import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


class Settings(BaseSettings):
    database_url: str


settings = Settings(
    database_url=os.getenv("DATABASE_URL", "")
)