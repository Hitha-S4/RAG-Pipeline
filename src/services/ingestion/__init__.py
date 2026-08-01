"""
Ingestion service package.

Sub-packages
────────────
    loaders/   — one loader per source type (PDF, Text, Markdown, HTML, CSV, JSON)
    chunkers/  — RecursiveChunker

Core modules
────────────
    ingestion_service.py — IngestionService (pipeline steps + orchestration)
    processor.py         — document cleaning / normalisation
    embedder.py          — multi-provider embedding service (AIM, OpenAI, HuggingFace)
    summarizer.py        — LLM per-chunk + rollup summarisation
    output_writer.py     — JSONL chunk dump + report
    markdown_service.py  — Markdown overview generation
    summary_writer.py    — summary JSONL + OVERVIEW.md
"""
from .ingestion_service import IngestionService

__all__ = [
    "IngestionService",
]

from .entity_pipeline import EntityPipeline  # window-based extraction flow
