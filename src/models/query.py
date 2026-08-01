"""
Query request / response models — basic ANN retrieval endpoint.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str
    top_k: int = Field(5, ge=1, le=50)
    filter_category: Optional[str] = None
    score_threshold: float = Field(0.0, ge=0.0, le=1.0)
    use_dfs: bool = False


class RetrievedChunk(BaseModel):
    chunk_id: str
    content: str
    summary: str = ""        # LLM-generated summary — used for embedding match context
    score: float = 0.0
    depth: int = 0
    is_leaf: bool = True
    parent_id: Optional[str] = None
    children_ids: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    ancestors: list["RetrievedChunk"] = Field(default_factory=list)
    descendants: list["RetrievedChunk"] = Field(default_factory=list)

    # Scoring internals — set by _rrf_search / rescore_and_rank.
    # Declared as proper fields so Pydantic v2 persists them on assignment;
    # excluded from the public JSON schema via exclude=True.
    summary_cos:     float = Field(default=0.0, exclude=True)
    score_breakdown: dict[str, Any] = Field(default_factory=dict, exclude=True)

    model_config = {"arbitrary_types_allowed": True}


# Resolve the self-referential forward references so Pydantic v2 can validate
# already-constructed RetrievedChunk instances when they appear as field values
# in other models (e.g. FacetDetail.chunks).
RetrievedChunk.model_rebuild()


class QueryResult(BaseModel):
    query: str
    rewritten_query: Optional[str] = None
    results: list[RetrievedChunk] = Field(default_factory=list)
    total: int = 0
