from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Database configuration
    DATABASE_URL: str = ""

    # Security configuration
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Encryption configuration
    ENCRYPTION_KEY: Optional[str] = None

    # Timezone configuration
    TIMEZONE: str = "America/Sao_Paulo"

    # Template configuration
    TEMPLATES_DIR: str = "app/templates"
    STATIC_DIR: str = "app/static"

    # Application configuration
    APP_NAME: str = "My FastAPI Application"
    DEBUG: bool = False

    # CORS configuration
    ALLOWED_HOSTS: list[str] = ["*"]
