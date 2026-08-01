"""PipelineContext — mutable state bag passed between pipeline steps."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.enums import IngestionStatus, SourceType
from src.models.chunk import Chunk
from src.models.document import Document


@dataclass
class PipelineContext:
    """Mutable bag of state passed between pipeline steps."""

    source:      str
    source_type: SourceType

    # Populated by the pipeline
    document:    Document | None   = None
    chunks:      list[Chunk]       = field(default_factory=list)
    classified:  list[dict]        = field(default_factory=list)  # classify_and_summarize output
    to_embed:    list[Chunk]       = field(default_factory=list)

    # Result tracking
    doc_id:      str              = field(default_factory=str)
    status:      IngestionStatus  = IngestionStatus.PENDING
    chunk_count: int              = 0
    error:       str              = ""
    started_at:  datetime         = field(default_factory=lambda: datetime.now(timezone.utc))
    finished_at: datetime | None  = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "doc_id":      self.doc_id,
            "source":      self.source,
            "status":      self.status.value,
            "chunk_count": self.chunk_count,
            "error":       self.error,
            "started_at":  self.started_at.isoformat(),
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
        }
