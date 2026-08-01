"""
Loader registry and factory.

Usage
─────
    from src.services.ingestion.loaders import get_loader
    from src.enums import SourceType

    loader   = get_loader(SourceType.PDF)
    document = loader.load("/path/to/file.pdf")

Supported sources
─────────────────
    SourceType.PDF      → PDFLoader      (formats/pdf.py)
    SourceType.TEXT     → TextLoader     (formats/text.py)
    SourceType.MARKDOWN → TextLoader     (formats/text.py)
    SourceType.HTML     → HTMLLoader     (formats/html.py)
    SourceType.CSV      → CSVLoader      (formats/csv.py)
    SourceType.JSON     → JSONLoader     (formats/json_loader.py)

Adding a new loader
───────────────────
    1. Create ``formats/<name>.py`` extending ``BaseLoader``.
    2. Add the mapping in ``_REGISTRY`` below.
    3. Add the new SourceType value to ``src/enums/source_type.py`` if needed.
"""
from __future__ import annotations

from src.enums import SourceType

from .formats import (
    CSVLoader,
    HTMLLoader,
    JSONLoader,
    LoaderProtocol,
    PDFLoader,
    TextLoader,
)

# ── Registry ──────────────────────────────────────────────────────────────────

_REGISTRY: dict[SourceType, type] = {
    SourceType.PDF:      PDFLoader,
    SourceType.TEXT:     TextLoader,
    SourceType.MARKDOWN: TextLoader,
    SourceType.HTML:     HTMLLoader,
    SourceType.CSV:      CSVLoader,
    SourceType.JSON:     JSONLoader,
}


def get_loader(source_type: SourceType) -> LoaderProtocol:
    """Return a fresh loader instance for *source_type*.

    Raises
    ------
    ValueError
        If no loader is registered for the requested source type.
    """
    cls = _REGISTRY.get(source_type)
    if cls is None:
        raise ValueError(f"No loader registered for source type: {source_type!r}")
    return cls()  # type: ignore[return-value]
