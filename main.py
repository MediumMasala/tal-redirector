"""
Tal Redirector - Production WhatsApp redirect microservice.

A reliable redirect service for WhatsApp deep links, handling
restrictive environments like LinkedIn's Android webview gracefully.

Run locally:
    uvicorn main:app --reload

Run in production:
    gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.config import settings
from app.logging_config import get_logger
from app.middleware import RequestTrackingMiddleware, SecurityHeadersMiddleware
from app.routes import router

logger = get_logger("main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup/shutdown events."""
    # Startup
    logger.info(
        "Starting Tal Redirector",
        extra={
            "version": __version__,
            "environment": settings.environment,
            "host": settings.host,
            "port": settings.port,
        },
    )
    yield
    # Shutdown
    logger.info("Shutting down Tal Redirector")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="WhatsApp redirect microservice with intelligent fallback for restrictive environments",
    version=__version__,
    docs_url="/docs" if settings.environment != "production" else None,
    redoc_url="/redoc" if settings.environment != "production" else None,
    openapi_url="/openapi.json" if settings.environment != "production" else None,
    lifespan=lifespan,
)

# =============================================================================
# Middleware (order matters - first added = outermost)
# =============================================================================

# Security headers
app.add_middleware(SecurityHeadersMiddleware)

# Request tracking and logging
app.add_middleware(RequestTrackingMiddleware)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# =============================================================================
# Routes
# =============================================================================

app.include_router(router)


# =============================================================================
# Entry point for direct execution
# =============================================================================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.environment == "development",
        log_level=settings.log_level.lower(),
    )
