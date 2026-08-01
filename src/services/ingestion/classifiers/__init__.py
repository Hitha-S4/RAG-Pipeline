"""
Classifiers — classification helpers for ingestion and retrieval.

Owns the two orthogonal classification axes:
    - Category  (ChunkCategory)  — what kind of information a chunk is
    - Sub-type  (ChunkSubType)   — which lifecycle action it covers

Also owns the end-to-end classify pipeline (LLM pass → per-chunk records).
"""
from .classify_service import ClassifyService
from .taxonomy import (
    primary_category,
    classify_sub_type,
    detect_query_sub_type,
    score_sub_types,
    valid_sub_type,
)

__all__ = [
    "ClassifyService",
    "primary_category",
    "classify_sub_type",
    "detect_query_sub_type",
    "score_sub_types",
    "valid_sub_type",
]
