from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    shortcut_api_key: str
    openai_api_key: str | None = None
    openai_model: str = "gpt-5.4-mini"
    app_timezone: str = "Asia/Taipei"
    monthly_income: str | None = None
    monthly_fixed_expenses: str | None = None

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
