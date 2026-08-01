"""HTML loader — strips tags via BeautifulSoup; also handles web URLs."""
from __future__ import annotations

from pathlib import Path

import httpx

from src.enums import SourceType
from src.models import Document, DocumentMetadata
from src.utils.logging import get_logger

from .base import BaseLoader

logger = get_logger(__name__)


class HTMLLoader(BaseLoader):
    """
    Loads HTML from a local file path **or** a remote URL, strips presentation
    noise (script, style, nav …) via BeautifulSoup, and returns plain text.
    """

    def get_supported_extensions(self) -> list[str]:
        return [".html", ".htm"]

    def load(self, source: str, **kwargs) -> Document:
        # URL sources skip file validation
        if not (source.startswith("http://") or source.startswith("https://")):
            self.validate_file(source)
        try:
            from bs4 import BeautifulSoup  # type: ignore
        except ImportError:
            raise RuntimeError("beautifulsoup4 is required: pip install beautifulsoup4")

        if source.startswith("http://") or source.startswith("https://"):
            resp = httpx.get(source, follow_redirects=True, timeout=30)
            resp.raise_for_status()
            raw_html = resp.text
            source_type = SourceType.URL
        else:
            raw_html = Path(source).read_text(encoding="utf-8", errors="replace")
            source_type = SourceType.HTML

        soup = BeautifulSoup(raw_html, "html.parser")
        for tag in soup(["script", "style", "header", "footer", "nav"]):
            tag.decompose()
        content = soup.get_text(separator="\n")

        logger.info("HTML loaded: %s  chars=%d", source, len(content))
        return Document(
            content=content,
            metadata=DocumentMetadata(
                source_name=source,
                source_type=source_type,
                url=source if source_type == SourceType.URL else "",
            ),
        )
