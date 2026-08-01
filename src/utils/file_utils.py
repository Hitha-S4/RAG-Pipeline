"""File system helpers for the ingestion pipeline."""
from __future__ import annotations

import os
import shutil
import uuid
from pathlib import Path

from src.config.settings import get_settings
from src.utils.logging import get_logger

logger = get_logger(__name__)


def get_upload_dir() -> Path:
    """Return the configured upload directory, creating it if needed."""
    path = Path(get_settings().upload_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_upload(filename: str, content: bytes) -> Path:
    """
    Persist an uploaded file under a UUID-prefixed name to avoid collisions.
    Returns the absolute path of the saved file.
    """
    upload_dir = get_upload_dir()
    safe_name  = f"{uuid.uuid4().hex}_{Path(filename).name}"
    dest       = upload_dir / safe_name
    dest.write_bytes(content)
    logger.info("Saved upload: %s  bytes=%d", dest, len(content))
    return dest


def delete_file(path: str | Path) -> None:
    """Delete a file if it exists."""
    p = Path(path)
    if p.exists():
        p.unlink()
        logger.debug("Deleted file: %s", p)


