"""
Chunkers package.

Public API
──────────
    from src.services.ingestion.chunkers import get_chunker, BaseChunker

    chunker = get_chunker(document)
    chunks  = chunker.chunk(document)
"""
from __future__ import annotations

from .strategies.base import BaseChunker
from .strategies.recursive_chunker import RecursiveChunker
from .factory import get_chunker

__all__ = [
    "BaseChunker",
    "RecursiveChunker",
    "get_chunker",
]
