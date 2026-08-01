"""
Agentic retrieval models — request / response types for the full whiteboard flow.
"""
from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from src.models.query import RetrievedChunk


class Intent(str, Enum):
    INFORMATIONAL = "informational"
    ACTION        = "action"


class TraversalStrategy(str, Enum):
    NONE = "none"
    DFS  = "dfs"
    BFS  = "bfs"
    BOTH = "both"


class Facets(BaseModel):
    keywords: list[str] = Field(default_factory=list)
    personas: list[str] = Field(default_factory=list)
    features: list[str] = Field(default_factory=list)
    entities: list[str] = Field(default_factory=list)

    def all_terms(self) -> list[str]:
        return list(dict.fromkeys(
            self.keywords + self.personas + self.features + self.entities
        ))


class FacetDetail(BaseModel):
    facet_type: str
    values:     list[str]             = Field(default_factory=list)
    chunks:     list[RetrievedChunk]  = Field(default_factory=list)


class PlanStep(BaseModel):
    order:           int
    action:          str
    detail:          str = ""
    source_chunk_id: str = ""


class WorkflowMatch(BaseModel):
    chunk_id:   str
    name:       str
    score:      float
    base_score: float = 0.0
    steps:      list[str]            = Field(default_factory=list)
    chunks:     list[RetrievedChunk] = Field(default_factory=list)


class AgenticQueryRequest(BaseModel):
    query:               str
    use_llm:             bool               = True
    top_k:               int                = Field(5, ge=1, le=50)
    score_threshold:     float              = Field(0.0, ge=0.0, le=1.0)
    facet_top_k:         int                = Field(3, ge=1, le=20)
    traversal:           TraversalStrategy  = TraversalStrategy.BOTH
    dfs_max_nodes:       int                = Field(20, ge=1, le=200)
    bfs_hops:            int                = Field(2, ge=1, le=25)
    max_traversal_nodes: int                = Field(40, ge=1, le=500)
    workflow_top_k:      int                = Field(3, ge=1, le=20)
    facet_boost:         float              = Field(0.15, ge=0.0, le=1.0)
    force_intent:        Optional[Intent]   = None
    force_sub_type:      Optional[str]      = None   # override lifecycle scope (install/configure/…)
    scope_by_sub_type:   bool               = True   # scope action retrieval by detected sub-type


class AgenticAnswer(BaseModel):
    query:                str
    rewritten_query:      str                   = ""
    multi_queries:        list[str]             = Field(default_factory=list)
    intent:               Optional[Intent]      = None
    intent_confidence:    float                 = 0.0
    sub_type:             Optional[str]         = None   # detected lifecycle scope
    facets:               Facets                = Field(default_factory=Facets)
    facet_details:        list[FacetDetail]     = Field(default_factory=list)
    answer:               str                   = ""
    supporting_chunks:    list[RetrievedChunk]  = Field(default_factory=list)
    matched_workflows:    list[WorkflowMatch]   = Field(default_factory=list)
    selected_workflow:    Optional[WorkflowMatch] = None
    plan:                 list[PlanStep]        = Field(default_factory=list)
    trace:                list[str]             = Field(default_factory=list)
    retrieval_top_score:  float                 = 0.0  # highest cosine score across all semantic searches


# Rebuild models that reference RetrievedChunk so forward references are fully
# resolved under `from __future__ import annotations`.
FacetDetail.model_rebuild()
WorkflowMatch.model_rebuild()
AgenticAnswer.model_rebuild()
