"""
Application-wide constants.

    EXT_TO_SOURCE_TYPE  — file-extension → SourceType mapping
    detect_source_type  — resolve a filename to its SourceType
"""
from __future__ import annotations

from pathlib import Path

from src.enums import SourceType

EXT_TO_SOURCE_TYPE: dict[str, SourceType] = {
    ".pdf":  SourceType.PDF,
    ".txt":  SourceType.TEXT,
    ".md":   SourceType.MARKDOWN,
    ".mdx":  SourceType.MARKDOWN,
    ".html": SourceType.HTML,
    ".htm":  SourceType.HTML,
    ".csv":  SourceType.CSV,
    ".json": SourceType.JSON,
}


def detect_source_type(filename: str) -> SourceType:
    """
    Resolve a filename to its :class:`~src.enums.SourceType`.

    Raises
    ------
    ValueError
        If the extension is not in :data:`EXT_TO_SOURCE_TYPE`.
    """
    ext = Path(filename).suffix.lower()
    source_type = EXT_TO_SOURCE_TYPE.get(ext)
    if source_type is None:
        supported = ", ".join(sorted(EXT_TO_SOURCE_TYPE))
        raise ValueError(
            f"Unsupported file extension: {ext!r}. Supported: {supported}"
        )
    return source_type
