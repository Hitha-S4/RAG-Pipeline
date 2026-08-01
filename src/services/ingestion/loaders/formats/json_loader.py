"""JSON loader — serialises a JSON file back to indented text."""
from __future__ import annotations

import json
from pathlib import Path

from src.enums import SourceType
from src.models import Document, DocumentMetadata
from src.utils.logging import get_logger

from .base import BaseLoader

logger = get_logger(__name__)


class JSONLoader(BaseLoader):
    """Reads a JSON file and pretty-prints it as indented text for downstream processing."""

    def get_supported_extensions(self) -> list[str]:
        return [".json"]

    def load(self, source: str, **kwargs) -> Document:
        self.validate_file(source)
        path = Path(source)
        data = json.loads(path.read_text(encoding="utf-8"))
        content = json.dumps(data, ensure_ascii=False, indent=2)
        logger.info("JSON loaded: %s  chars=%d", path.name, len(content))
        return Document(
            content=content,
            metadata=DocumentMetadata(
                source_name=path.stem,
                source_type=SourceType.JSON,
                original_filename=path.name,
            ),
        )
