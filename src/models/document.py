"""Document models — source provenance and raw loaded content."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from src.enums import SourceType


@dataclass
class DocumentMetadata:
    source_name:       str             = ""
    source_type:       SourceType      = SourceType.TEXT
    original_filename: str             = ""
    url:               str             = ""
    created_at:        datetime        = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    extra:             dict[str, Any]  = field(default_factory=dict)


@dataclass
class Document:
    content:         str
    doc_id:          str              = field(default_factory=lambda: str(uuid4()))
    metadata:        DocumentMetadata = field(default_factory=DocumentMetadata)
    cleaned_content: str              = ""
