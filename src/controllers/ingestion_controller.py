"""
Ingestion controller — FastAPI routes for data ingestion.

Endpoints
─────────
    POST   /ingest/file         Upload a file (PDF, TXT, MD, HTML, CSV, JSON)
    DELETE /ingest/collection   Drop the entire Milvus collection
"""
from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from src.utils.constants import detect_source_type
from src.config.settings import get_settings
from src.models import IngestResponse
from src.services.ingestion import IngestionService
from src.utils.file_utils import save_upload, delete_file
from src.utils.logging import get_logger

router   = APIRouter(prefix="/ingest", tags=["Ingestion"])
logger   = get_logger(__name__)
_service = IngestionService()


# ── Helpers ───────────────────────────────────────────────────────────────────

def _resolve_source_type(filename: str):
    """Wrap detect_source_type, converting ValueError to HTTP 415."""
    try:
        return detect_source_type(filename)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=str(exc),
        )


def _check_file_size(size_bytes: int) -> None:
    max_bytes = get_settings().max_upload_size_mb * 1024 * 1024
    if size_bytes > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File exceeds maximum size of {get_settings().max_upload_size_mb} MB",
        )


# ── Routes ────────────────────────────────────────────────────────────────────

@router.post(
    "/file",
    response_model=IngestResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Ingest an uploaded file",
)
async def ingest_file(
    file: Annotated[UploadFile, File(description="File to ingest")]
):
    """
    Upload a file (PDF, TXT, MD, HTML, CSV, JSON) and run the full
    ingestion pipeline asynchronously.
    """
    content = await file.read()
    _check_file_size(len(content))

    source_type = _resolve_source_type(file.filename or "unknown")
    saved_path  = save_upload(file.filename or "upload", content)

    try:
        result = await _service.ingest(
            source=str(saved_path),
            source_type=source_type,
        )
    finally:
        delete_file(saved_path)   # clean up temp file regardless of outcome

    if result.status.value == "failed":
        raise HTTPException(status_code=500, detail=result.error)

    return IngestResponse(**result.to_dict())


@router.delete(
    "/collection",
    summary="Drop the entire Milvus collection",
)
async def drop_collection():
    """Drop the entire vector store collection. It is recreated automatically on next ingest."""
    from src.services.vectordb.milvus_service import MilvusService
    vectordb = MilvusService()
    result = await vectordb.drop_collection()
    return result
