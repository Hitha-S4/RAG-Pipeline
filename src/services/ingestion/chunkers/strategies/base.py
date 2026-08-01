"""
Abstract base class for all chunking strategies.

Every concrete chunker must implement :meth:`BaseChunker.chunk`, which takes a
processed :class:`~src.models.Document` and returns a list of
:class:`~src.models.Chunk` objects.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from src.models import Chunk, Document


class BaseChunker(ABC):
    """Contract for chunking strategies."""

    @abstractmethod
    def chunk(self, document: Document) -> list[Chunk]:
        """
        Split *document* into a list of :class:`Chunk` objects.

        Parameters
        ----------
        document:
            A ``Document`` whose ``cleaned_content`` has already been populated
            by the processor step.

        Returns
        -------
        list[Chunk]
            Ordered list of chunks ready for embedding and storage.
        """
