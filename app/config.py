"""
Application configuration using Pydantic Settings.

Configuration is loaded from environment variables with sensible defaults.
"""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "Tal Redirector"
    app_version: str = "1.0.0"
    environment: str = "development"  # development, staging, production
    debug: bool = False

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"  # json or text

    # Security
    allowed_origins: List[str] = ["*"]
    rate_limit_requests: int = 100
    rate_limit_window: int = 60  # seconds

    # WhatsApp defaults
    default_whatsapp_message: str = ""

    # Phone validation
    phone_min_length: int = 10
    phone_max_length: int = 15

    # Feature flags
    enable_metrics: bool = True
    enable_request_logging: bool = True


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
