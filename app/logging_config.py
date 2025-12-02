"""
Structured logging configuration for production.

Supports JSON format for log aggregation (ELK, CloudWatch, etc.)
and text format for local development.
"""

import logging
import sys
from datetime import datetime, timezone
from typing import Any, Dict

from pythonjsonlogger import jsonlogger

from app.config import settings


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter with additional fields."""

    def add_fields(
        self,
        log_record: Dict[str, Any],
        record: logging.LogRecord,
        message_dict: Dict[str, Any],
    ) -> None:
        super().add_fields(log_record, record, message_dict)

        # Add timestamp in ISO format
        log_record["timestamp"] = datetime.now(timezone.utc).isoformat()

        # Add log level
        log_record["level"] = record.levelname

        # Add service info
        log_record["service"] = settings.app_name
        log_record["environment"] = settings.environment

        # Add source info
        log_record["logger"] = record.name
        log_record["module"] = record.module
        log_record["function"] = record.funcName
        log_record["line"] = record.lineno

        # Remove default fields we've replaced
        log_record.pop("levelname", None)
        log_record.pop("asctime", None)


def setup_logging() -> logging.Logger:
    """
    Configure application logging.

    Returns the root logger configured for the application.
    """
    # Get root logger
    logger = logging.getLogger("tal_redirector")
    logger.setLevel(getattr(logging, settings.log_level.upper()))

    # Remove existing handlers
    logger.handlers.clear()

    # Create handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(getattr(logging, settings.log_level.upper()))

    # Set formatter based on config
    if settings.log_format == "json":
        formatter = CustomJsonFormatter(
            "%(timestamp)s %(level)s %(name)s %(message)s"
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


# Create module-level logger
logger = setup_logging()


def get_logger(name: str) -> logging.Logger:
    """Get a child logger with the given name."""
    return logger.getChild(name)
