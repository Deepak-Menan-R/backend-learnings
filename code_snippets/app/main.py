from fastapi import FastAPI
from app.api.health import router as health_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Health Service",
        version="1.0.0"
    )

    # Include routers
    app.include_router(health_router, prefix="/api")

    return app

app = create_app()