"""
Basic retrieval service — ANN search with optional DFS tree expansion.

Used for simple top-K lookups (the /api/v1/query endpoint).
For the full agentic flow (rewrite → facets → intent → plan) use
AgenticRetrievalService instead.
"""
from __future__ import annotations

from src.models.query import QueryRequest, QueryResult, RetrievedChunk
from src.services.ingestion.embedders import EmbeddingService
from src.services.vectordb.milvus_service import MilvusService
from src.utils.logging import get_logger

logger = get_logger(__name__)


class RetrievalService:
    def __init__(self):
        self._embedder = EmbeddingService()
        self._vectordb = MilvusService()

    async def query(self, request: QueryRequest) -> QueryResult:
        filters: list[str] = []
        if request.filter_category:
            filters.append(f'chunk_type == "{request.filter_category}"')
        filter_expr = " && ".join(filters)

        logger.info(
            "Retrieval  query='%s'  top_k=%d  filter='%s'  dfs=%s",
            request.query, request.top_k, filter_expr, request.use_dfs,
        )
        query_vector = self._embedder.embed_query(request.query)

        hits = await self._vectordb.search(
            query_vector=query_vector,
            top_k=request.top_k,
            filter_expr=filter_expr,
            score_threshold=request.score_threshold,
        )

        if hits:
            scores = [h.score for h in hits]
            logger.info(
                "cosine scores  hits=%d  top=%.4f (%.1f%%)  mean=%.4f (%.1f%%)  min=%.4f (%.1f%%)",
                len(hits),
                scores[0],  scores[0]  * 100,
                sum(scores) / len(scores), sum(scores) / len(scores) * 100,
                scores[-1], scores[-1] * 100,
            )

        if request.use_dfs and hits:
            hits = await self._expand_dfs(hits)

        logger.info("Retrieved %d results", len(hits))
        return QueryResult(query=request.query, results=hits, total=len(hits))

    async def _expand_dfs(self, hits: list[RetrievedChunk]) -> list[RetrievedChunk]:
        """For each ANN hit attach its ancestor path and full DFS descendant subtree."""
        expanded: list[RetrievedChunk] = []
        for hit in hits:
            ancestors = await self._vectordb.fetch_ancestors(hit.chunk_id)

            descendants: list[RetrievedChunk] = []
            for child_id in hit.children_ids:
                subtree = await self._vectordb.fetch_subtree(child_id)
                descendants.extend(subtree)

            hit.ancestors   = ancestors
            hit.descendants = descendants
            expanded.append(hit)

            logger.debug(
                "DFS expanded  chunk=%s  ancestors=%d  descendants=%d",
                hit.chunk_id, len(ancestors), len(descendants),
            )
        return expanded
