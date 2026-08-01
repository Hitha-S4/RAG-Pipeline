"""
Central router registry — single place to register all API routes.

All sub-routers are mounted under the ``/api/v1`` prefix here.
To add a new controller:
    1. Create ``src/controllers/<name>_controller.py`` with its own APIRouter.
    2. Import it below and call ``api_router.include_router()``.
"""
from __future__ import annotations

from fastapi import APIRouter

from src.controllers.health_controller import router as health_router
from src.controllers.ingestion_controller import router as ingestion_router
from src.controllers.retrieval_controller import router as retrieval_router

# Root versioned router — every endpoint is mounted under /api/v1
api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(ingestion_router)
api_router.include_router(retrieval_router)
