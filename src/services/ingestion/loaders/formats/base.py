"""
Shared base types for all document loaders.

    BaseLoader        — abstract base class every loader should extend
    LoaderProtocol    — structural typing interface (for type-checking only)

Document and DocumentMetadata have moved to src.models.document.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Protocol

from src.models.document import Document, DocumentMetadata  # noqa: F401 — re-exported


class BaseLoader(ABC):
    """Abstract base for all document loaders."""

    @abstractmethod
    def load(self, source: str, **kwargs) -> Document:
        """Load document content from *source* (file path or URL) and return a Document."""

    @abstractmethod
    def get_supported_extensions(self) -> list[str]:
        """Return the list of file extensions this loader handles (e.g. ['.pdf'])."""

    def can_load(self, source: str) -> bool:
        """Return True if this loader supports the given file path."""
        return Path(source).suffix.lower() in [
            ext.lower() for ext in self.get_supported_extensions()
        ]

    def validate_file(self, source: str) -> None:
        """
        Validate that *source* exists, is a file, and is supported.

        Raises
        ------
        FileNotFoundError
            If the path does not exist.
        ValueError
            If the path is not a file or the extension is unsupported.
        """
        path = Path(source)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        if not path.is_file():
            raise ValueError(f"Path is not a file: {path}")
        if not self.can_load(source):
            raise ValueError(
                f"Unsupported file type: {path.suffix}. "
                f"Supported: {', '.join(self.get_supported_extensions())}"
            )


class LoaderProtocol(Protocol):
    """Structural typing interface — use BaseLoader for concrete loaders."""

    def load(self, source: str, **kwargs) -> Document: ...
