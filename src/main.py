"""
RAG Pipeline — FastAPI application entry point.
"""
from __future__ import annotations

import os
import sys

# Make sure `src` is importable when running `python main.py`
sys.path.insert(0, os.path.dirname(__file__))

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.config.settings import get_settings
from src.controllers import api_router
from src.utils.logging import get_logger

logger = get_logger(__name__)


# ── Lifespan (startup / shutdown) ─────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    logger.info(
        "Starting %s  env=%s  milvus_mode=%s",
        settings.app_name, settings.app_env, settings.milvus_mode,
    )
    # Eagerly initialise the upload directory
    from src.utils.file_utils import get_upload_dir
    get_upload_dir()
    yield
    logger.info("%s shutting down", settings.app_name)


# ── App factory ───────────────────────────────────────────────────────────────

def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        description=(
            "Production-ready RAG ingestion pipeline.\n\n"
            "Supports PDF, Text, Markdown, HTML, CSV, and JSON sources.\n"
            "Vector store: Milvus Lite (embedded) or Milvus Standalone (remote)."
        ),
        version="1.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # ── CORS ──────────────────────────────────────────────────────────────────
    # The CORS spec forbids allow_origins=["*"] combined with
    # allow_credentials=True — browsers reject such responses.
    # In non-production we use allow_origin_regex to accept every origin
    # while still echoing back the concrete requesting origin, which
    # satisfies both the browser and the credentials flag.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[] if settings.app_env == "production" else [],
        allow_origin_regex=r".*" if settings.app_env != "production" else None,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    # ── Routers ───────────────────────────────────────────────────────────────
    app.include_router(api_router)   # all routes mounted under /api/v1

    # ── UI (test_query/ui.html served at /ui) ─────────────────────────────────
    _ui_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_query")
    if os.path.isdir(_ui_dir):
        app.mount("/ui", StaticFiles(directory=_ui_dir, html=True), name="ui")

        @app.get("/ui", include_in_schema=False)
        async def _ui_redirect():
            return RedirectResponse(url="/ui/ui.html")

    return app


app = create_app()
