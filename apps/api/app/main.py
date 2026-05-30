from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.newsletters import router as newsletters_router
from app.core.config import settings
from app.db import init_db


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


def create_app(*, auto_create_tables: bool = True) -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan if auto_create_tables else None)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health_router)
    app.include_router(newsletters_router)
    return app


app = create_app()
