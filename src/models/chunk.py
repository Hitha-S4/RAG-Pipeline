"""Chunk domain model.

N-level hierarchical chunk tree:
    depth=1  L1 heading (root)
    depth=2  L2 section
    depth=3  L3 subsection
    depth=4  L4 sub-subsection
    depth=5  leaf (actual content, is_leaf=True)

parent_id / children_ids maintain the full parent → child tree.
content_hash enables deduplication and change-detection on re-ingest.

NEW (dual-vector design)
────────────────────────
Every chunk now carries BOTH:
    content            + embedding            → verbatim text vector
    summary            + summary_embedding    → abstractive gist vector

Leaf summaries are produced per-chunk by the SummarizerService; branch summaries
are produced by rolling up children's summaries. Storing both vectors lets the
retriever match a query against exact wording OR high-level meaning.
"""
from __future__ import annotations

import hashlib
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field, computed_field, model_validator

from src.enums import ChunkCategory


class ChunkMetadata(BaseModel):
    """Semantic / structural metadata — no provenance fields here."""
    chunk_type:    ChunkCategory = ChunkCategory.KNOWLEDGE
    sub_type:      str           = ""
    headings:      list[str]     = Field(default_factory=list)
    depth:         int           = 1
    is_leaf:       bool          = True
    parent_id:     Optional[str] = None
    children_ids:  list[str]     = Field(default_factory=list)


class Chunk(BaseModel):

    # ── Identity ──────────────────────────────────────────────────────────────
    chunk_id:     str  = Field(default_factory=lambda: str(uuid4()))

    # ── Content ───────────────────────────────────────────────────────────────
    content:      str
    content_hash: str  = ""          # set by model_validator after content is known

    # ── Summary (abstractive gist — filled by SummarizerService) ──────────────
    summary:      str  = ""

    # ── Facets (LLM-extracted) ────────────────────────────────────────────────
    # Two jobs:
    #   1. cross-category links: persona -> feature -> workflow -> knowledge
    #   2. the lexical/facet term of the relevance score, which is what anchors
    #      rare tokens ("S-GATE") that dense vectors blur away.
    keywords:  list[str] = Field(default_factory=list)
    features:  list[str] = Field(default_factory=list)
    workflows: list[str] = Field(default_factory=list)
    personas:  list[str] = Field(default_factory=list)
    entities:  list[str] = Field(default_factory=list)

    # ── Structure ─────────────────────────────────────────────────────────────
    metadata:     ChunkMetadata = Field(default_factory=ChunkMetadata)

    # ── Vectors ───────────────────────────────────────────────────────────────
    embedding:         list[float] = Field(default_factory=list)  # of `content`
    summary_embedding: list[float] = Field(default_factory=list)  # of `summary`

    # ── Computed ──────────────────────────────────────────────────────────────
    @computed_field  # type: ignore[misc]
    @property
    def token_count(self) -> int:
        return max(1, int(len(self.content) / 4.5))

    @model_validator(mode="after")
    def _set_content_hash(self) -> "Chunk":
        if not self.content_hash:
            self.content_hash = hashlib.sha256(self.content.encode()).hexdigest()
        return self

    # ── Convenience shortcuts (avoid .metadata.xxx everywhere) ────────────────
    @property
    def depth(self) -> int:
        return self.metadata.depth

    @property
    def is_leaf(self) -> bool:
        return self.metadata.is_leaf

    @property
    def parent_id(self) -> Optional[str]:
        return self.metadata.parent_id

    @property
    def children_ids(self) -> list[str]:
        return self.metadata.children_ids

    @property
    def chunk_type(self) -> ChunkCategory:
        return self.metadata.chunk_type
