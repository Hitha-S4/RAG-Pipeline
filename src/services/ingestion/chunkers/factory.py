"""
Chunker factory — registry-based strategy selection.

Adding a new strategy
─────────────────────
    1. Create ``chunkers/strategies/<name>.py`` implementing ``BaseChunker``.
    2. Add an entry to ``_REGISTRY`` mapping the strategy name to the class.
    3. Set ``CHUNK_STRATEGY=<name>`` in .env to activate it.
"""
from __future__ import annotations

from typing import Type

from src.config.settings import get_settings
from src.models import Document

from .strategies.base import BaseChunker
from .strategies.recursive_chunker import RecursiveChunker

# ── Registry ──────────────────────────────────────────────────────────────────
# Map strategy name → chunker class.  Add new strategies here.

_REGISTRY: dict[str, Type[BaseChunker]] = {
    "recursive": RecursiveChunker,
}


def get_chunker(document: Document, strategy: str | None = None) -> BaseChunker:
    """
    Instantiate and return the chunker for *strategy*.

    Falls back to ``settings.chunk_strategy`` when *strategy* is ``None``.
    Raises ``ValueError`` for unknown strategy names.
    """
    key = (strategy or get_settings().chunk_strategy).lower()
    cls = _REGISTRY.get(key)
    if cls is None:
        raise ValueError(
            f"Unknown chunk strategy: {key!r}. "
            f"Available: {', '.join(_REGISTRY)}"
        )
    return cls()
