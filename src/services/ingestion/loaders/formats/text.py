"""Text / Markdown loader — reads plain .txt, .md, and .mdx files."""
from __future__ import annotations

from pathlib import Path

from src.enums import SourceType
from src.models import Document, DocumentMetadata
from src.utils.logging import get_logger

from .base import BaseLoader

logger = get_logger(__name__)


class TextLoader(BaseLoader):
    """Loads plain-text or Markdown files from the local filesystem."""

    def get_supported_extensions(self) -> list[str]:
        return [".txt", ".md", ".mdx"]

    def load(self, source: str, **kwargs) -> Document:
        self.validate_file(source)
        path = Path(source)
        content = path.read_text(encoding="utf-8", errors="replace")
        source_type = (
            SourceType.MARKDOWN
            if path.suffix.lower() in {".md", ".mdx"}
            else SourceType.TEXT
        )
        logger.info("Text loaded: %s  chars=%d", path.name, len(content))
        return Document(
            content=content,
            metadata=DocumentMetadata(
                source_name=path.stem,
                source_type=source_type,
                original_filename=path.name,
            ),
        )
