"""
Ingestion request / response models.

    IngestResponse  — response for POST /ingest/file
"""
from __future__ import annotations

from pydantic import BaseModel


class IngestResponse(BaseModel):
    doc_id:      str
    source:      str
    status:      str
    chunk_count: int
    error:       str = ""
