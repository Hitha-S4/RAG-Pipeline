"""
Retrieval controller — two query endpoints.

POST /api/v1/query          Basic ANN search (top-K chunks, optional DFS expansion)
POST /api/v1/query/agentic  Full agentic flow:
                              rewrite → facets → intent detection →
                              informational answer  OR  workflow plan
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from src.models.agentic import AgenticAnswer, AgenticQueryRequest
from src.models.query import QueryRequest, QueryResult
from src.services.retrieval.agentic_retrieval_service import AgenticRetrievalService
from src.services.retrieval.retrieval_service import RetrievalService
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/query", tags=["retrieval"])

# Singletons — created once, reused across requests
_basic_svc:   RetrievalService | None = None
_agentic_svc: AgenticRetrievalService | None = None


def _get_basic() -> RetrievalService:
    global _basic_svc
    if _basic_svc is None:
        _basic_svc = RetrievalService()
    return _basic_svc


def _get_agentic() -> AgenticRetrievalService:
    global _agentic_svc
    if _agentic_svc is None:
        _agentic_svc = AgenticRetrievalService()
    return _agentic_svc


@router.post("", response_model=QueryResult, summary="Basic ANN search")
async def query(request: QueryRequest) -> QueryResult:
    """
    Top-K vector search over ingested chunks.

    - **query**: natural-language question or search phrase
    - **top_k**: number of results (default 5)
    - **filter_category**: restrict to one category
      (`knowledge` | `features` | `workflows` | `entities` | `keywords` | `personas`)
    - **score_threshold**: minimum cosine similarity (0–1)
    - **use_dfs**: expand each hit with its ancestor path + full descendant subtree
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")
    try:
        return await _get_basic().query(request)
    except Exception as exc:
        logger.error("Basic query failed: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail=str(exc))


@router.post("/agentic", response_model=AgenticAnswer, summary="Agentic retrieval")
async def agentic_query(request: AgenticQueryRequest) -> AgenticAnswer:
    """
    Full agentic retrieval flow (whiteboard pipeline):

    1. **Rewrite** the question using Knowledge Base context
    2. **Extract** Keywords, Personas, Features (+ KB grounding)
    3. **Fetch** details of each facet semantically
    4. **Detect intent** — informational vs action
       - *Informational* → synthesise an answer from retrieved context
       - *Action* → match workflows → fetch via DFS → create an execution plan

    Set `use_llm=false` to run the full pipeline with heuristic fallbacks only
    (no AIM calls — useful for testing without the endpoint).

    Set `force_intent` to `"action"` or `"informational"` to bypass auto-detection.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="query must not be empty")
    try:
        return await _get_agentic().run(request)
    except Exception as exc:
        logger.error("Agentic query failed: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail=str(exc))
