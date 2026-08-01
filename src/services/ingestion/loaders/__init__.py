"""Loaders package — public API."""
from __future__ import annotations

from src.models import Document, DocumentMetadata

from .formats import *  # noqa: F401, F403  — formats/__init__.__all__ is the source of truth
from .loader import get_loader

__all__ = [
    "Document",
    "DocumentMetadata",
    "get_loader",
    # loader classes re-exported via formats.*
]
