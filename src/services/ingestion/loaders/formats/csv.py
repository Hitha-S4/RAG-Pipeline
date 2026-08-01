"""CSV loader — converts each row to a key: value text block."""
from __future__ import annotations

import csv
from pathlib import Path

from src.enums import SourceType
from src.models import Document, DocumentMetadata
from src.utils.logging import get_logger

from .base import BaseLoader

logger = get_logger(__name__)


class CSVLoader(BaseLoader):
    """Reads a CSV file and converts every row into a ``key: value`` text block."""

    def get_supported_extensions(self) -> list[str]:
        return [".csv"]

    def load(self, source: str, **kwargs) -> Document:
        self.validate_file(source)
        path = Path(source)
        rows: list[str] = []

        with path.open(encoding="utf-8", errors="replace", newline="") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                rows.append("  ".join(f"{k}: {v}" for k, v in row.items()))

        content = "\n".join(rows)
        logger.info("CSV loaded: %s  rows=%d", path.name, len(rows))
        return Document(
            content=content,
            metadata=DocumentMetadata(
                source_name=path.stem,
                source_type=SourceType.CSV,
                original_filename=path.name,
            ),
        )
