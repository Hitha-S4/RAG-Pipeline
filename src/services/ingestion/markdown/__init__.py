"""
Markdown generation package.

Public API
──────────
    from src.services.ingestion.markdown import MarkdownService

Package layout
──────────────
    helpers.py                — low-level, stateless text utilities
    pipeline.py               — RAW.md builder, concise builder, knowledge-context reader
    service.py                — MarkdownService orchestrator
    chunk_summary_pipeline.py — two-phase AIM summarisation pipeline (CLI + library)
"""
from .service import MarkdownService
from .helpers import DOC_NAME_FALLBACK, MAX_RAW_BODY
from .chunk_summary_pipeline import ChunkSummaryPipeline

__all__ = [
    "MarkdownService",
    "DOC_NAME_FALLBACK",
    "MAX_RAW_BODY",
    "ChunkSummaryPipeline",
]
