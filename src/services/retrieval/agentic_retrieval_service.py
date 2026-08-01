"""
Agentic retrieval service — implements the full whiteboard retrieval flow.

Flow
────
    Question
      ↓
    [1] Rewrite + multi-query expansion
          Rewrite with KNOWLEDGE.md + ENTITIES.md + top KNOWLEDGE vector chunks.
          Expand into N variants: original, rewritten, + LLM reformulations
          (synonyms, acronym expansions, perspective shifts, HyDE-style).
      ↓
    [1b] RAG-Fusion setup
          multi_queries = [original, rewritten, llm_variant_1, …, llm_variant_4]
      ↓
    [2] Extract Keywords, Personas, Features, Entities (+ KB examples from MD files)
      ↓
    [3] RRF Fetch facet details
          Each facet category searched with all multi_queries concurrently.
          Reciprocal Rank Fusion merges ranked lists → BFS breadth expansion.
      ↓
    [4] Intent + sub-type detection
      ↓
    [5] Branch
          │
          ├── INFORMATIONAL → [5a] RAG-Fusion answer
          │     All multi_queries searched concurrently over
          │     keywords/features/entities/knowledge categories.
          │     RRF fuses ranks → intent-aware block bias →
          │     DFS/BFS traversal → IDF rescore → LLM synthesise.
          │
          └── ACTION → [5b] Workflow → plan
                Workflow search uses augmented query (facet-boosted).
                DFS ordered steps extracted from top-K matched workflows.
                Whiteboard boxed step: RRF fetch Knowledge + Keywords +
                Personas + Features + Entities as enrichment context.
                synthesize_plan(steps, context) → LLM plan grounded in
                both the workflow steps AND the enrichment context.
                Falls back to synthesize_answer(context) when no steps.
                Execute & React: plan handed off to workflow executor.
"""
from __future__ import annotations

import asyncio
import os
import re
from collections import defaultdict
from typing import Optional

from src.config.settings import get_settings
from src.enums import ChunkCategory
from src.models.agentic import (
    AgenticAnswer,
    AgenticQueryRequest,
    Facets,
    FacetDetail,
    Intent,
    PlanStep,
    TraversalStrategy,
    WorkflowMatch,
)
from src.models.query import RetrievedChunk
from src.services.retrieval import ranking
from src.services.retrieval.graph_traversal import ChunkGraphTraversal
from src.services.retrieval.query_understanding import QueryUnderstanding
from src.utils.logging import get_logger

logger = get_logger(__name__)

# ── Stop-word filtering for cosine search ────────────────────────────────────
# Removing function words from the query vector improves cosine similarity
# because the embedding space aligns "K-TAP" with stored "K-TAP" chunks more
# tightly than "What is K-TAP?" (where "what", "is" pull the vector toward
# generic question embeddings).  The original full query is always kept for
# LLM synthesis so the answer is still generated against the real question.

_STOP_WORDS = frozenset({
    # question words
    "what", "which", "who", "whom", "whose", "where", "when", "why", "how",
    # auxiliary / copula
    "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "have", "has", "had",
    "can", "could", "will", "would", "shall", "should", "may", "might", "must",
    # articles & determiners
    "a", "an", "the", "this", "that", "these", "those",
    # prepositions & conjunctions
    "in", "on", "at", "by", "for", "with", "about", "from", "to", "of",
    "and", "or", "but", "if", "as", "than", "so",
    # common fillers
    "i", "me", "my", "you", "your", "it", "its", "we", "our", "they",
    "there", "here", "please", "tell", "me", "give",
    "explain", "describe", "define", "list", "show",
})

_WORD_RE = re.compile(r"[\w\-]+")   # keep hyphenated tokens like K-TAP, S-TAP intact


def _strip_stop_words(text: str) -> str:
    """Return *text* with English stop words removed.

    Preserves hyphenated tokens verbatim (K-TAP, S-TAP, A-TAP …) and falls
    back to the original string when the result would be empty.

    Examples
    --------
    "What is K-TAP?"        → "K-TAP"
    "How do I install GIM?" → "install GIM"
    "define S-TAP agent"    → "S-TAP agent"
    """
    tokens = _WORD_RE.findall(text)
    kept = [t for t in tokens if t.lower() not in _STOP_WORDS]
    return " ".join(kept) if kept else text


_FACET_CATEGORIES = {
    "keywords": ChunkCategory.KEYWORDS.value,
    "personas": ChunkCategory.PERSONAS.value,
    "features": ChunkCategory.FEATURES.value,
    "entities": ChunkCategory.ENTITIES.value,
}

# Requirement (4): an INFORMATIONAL question (no action / no workflow) is answered
# from keywords + features + entities + knowledge only.  An ACTION question adds
# workflows (the steps) and personas (who performs them).
_INFORMATIONAL_CATS = [
    ChunkCategory.KNOWLEDGE.value,
    ChunkCategory.FEATURES.value,
    ChunkCategory.ENTITIES.value,
    ChunkCategory.KEYWORDS.value,
]
_ACTION_EXTRA_CATS = [
    ChunkCategory.WORKFLOWS.value,
    ChunkCategory.PERSONAS.value,
]

# Summary files that live in uploads/summary/
_SUMMARY_FILES = {
    "knowledge":  "KNOWLEDGE.md",
    "keywords":   "KEYWORDS.md",
    "personas":   "PERSONAS.md",
    "features":   "FEATURES.md",
    "workflows":  "WORKFLOWS.md",
    "entities":   "ENTITIES.md",
}


class AgenticRetrievalService:
    """
    Orchestrates the multi-step agentic retrieval flow.

    All heavy dependencies are injectable so the pipeline can be exercised
    without Milvus or an LLM (pass fakes in tests).
    """

    def __init__(self, embedder=None, vectordb=None, understander=None):
        if embedder is None:
            from src.services.ingestion.embedders import EmbeddingService
            embedder = EmbeddingService()
        if vectordb is None:
            from src.services.vectordb.milvus_service import MilvusService
            vectordb = MilvusService()
        if understander is None:
            understander = QueryUnderstanding()

        self._embedder    = embedder
        self._vdb         = vectordb
        self._llm         = understander
        self._graph       = ChunkGraphTraversal(vectordb)
        settings          = get_settings()
        self._summary_dir = getattr(settings, "summary_dir", "uploads/summary")

    # ── Public entry point ────────────────────────────────────────────────────

    async def run(self, request: AgenticQueryRequest) -> AgenticAnswer:
        trace: list[str] = []
        q = request.query.strip()
        trace.append(f"question: {q!r}")
        self._retrieval_top_score: float = 0.0   # reset per request
        # Tracks the top-cosine chunk seen across every _semantic_search call.
        # Stored as (chunk, raw_cosine) tuples so the raw float is captured
        # immutably — chunk.score may be overwritten later by rescore_and_rank.
        self._top_cosine_chunks: dict[str, tuple[RetrievedChunk, float]] = {}

        # ── [1] Rewrite with Knowledge Base + entity context ──────────────────
        # Combine KNOWLEDGE.md + ENTITIES.md + top semantic KNOWLEDGE chunks
        kb_file_ctx       = self._read_summary_file("knowledge")
        entities_file_ctx = self._read_summary_file("entities")
        kb_vec_ctx       = await self._kb_vector_context(q, k=4)
        kb_context       = (kb_file_ctx + "\n\n" + kb_vec_ctx).strip() if kb_file_ctx else kb_vec_ctx
        if entities_file_ctx:
            kb_context = kb_context + "\n\nENTITIES:\n" + entities_file_ctx

        rewritten = self._llm.rewrite_query(q, kb_context) if request.use_llm else q
        trace.append(
            f"rewrote query → {rewritten!r}"
            if rewritten != q else "rewrite: unchanged"
        )

        # ── [1b] Multi-query expansion (up to 5 variants of the rewritten query) ─
        _llm_queries = (
            self._llm.generate_multi_queries(rewritten)
            if request.use_llm else [rewritten]
        )
        # Prepend original question + rewritten query; deduplicate while preserving order
        _seen: set[str] = set()
        multi_queries: list[str] = []
        for _qv in [q, rewritten] + _llm_queries:
            if _qv.lower() not in _seen:
                _seen.add(_qv.lower())
                multi_queries.append(_qv)
        trace.append(f"multi_queries ({len(multi_queries)}): {multi_queries}")

        # ── [2] Extract Keywords, Personas, Features (+ KB + MD examples) ─────
        # Build rich context: KB overview + real term examples per category
        md_facet_ctx  = self._load_facet_examples()
        facet_context = self._build_facet_context(kb_context, md_facet_ctx)
        facets = await self._extract_facets(rewritten, facet_context, request)
        trace.append(
            f"facets: keywords={facets.keywords} "
            f"personas={facets.personas} features={facets.features} "
            f"entities={facets.entities}"
        )

        # ── [3] (Semantic) Fetch details of each facet ────────────────────────
        # Intent is not yet determined here; pass None so _rrf_search runs pure RRF
        # without block bias (bias is applied in _answer_branch where intent is known).
        facet_details = await self._fetch_facet_details(
            rewritten, facets, request,
            multi_queries=multi_queries,
            intent_label=None,
        )
        trace.append(
            "facet details fetched: "
            + ", ".join(f"{d.facet_type}={len(d.chunks)}" for d in facet_details)
        )

        # ── [4] Is the user asking to take an action? ─────────────────────────
        if request.force_intent is not None:
            intent, conf = request.force_intent, 1.0
            trace.append(f"intent: forced → {intent.value}")
        else:
            label, conf = ranking.detect_action_intent(rewritten)
            intent = Intent.ACTION if label == "action" else Intent.INFORMATIONAL
            trace.append(f"intent: {intent.value} (confidence={conf:.2f})")

        # Detect the lifecycle sub-type the question is about (install/configure/…)
        # so the ACTION branch can scope persona/feature/workflow retrieval to it
        # (requirement 3: "how to configure collector?" → configure slice).
        from src.services.ingestion.classifiers import detect_query_sub_type, valid_sub_type
        if request.force_sub_type:
            sub = valid_sub_type(request.force_sub_type)
            sub_type = sub.value
        else:
            detected = detect_query_sub_type(rewritten)
            sub_type = detected.value if detected else None
        if sub_type:
            trace.append(f"sub_type: {sub_type}")

        answer = AgenticAnswer(
            query=q,
            rewritten_query=rewritten,
            multi_queries=multi_queries,
            intent=intent,
            intent_confidence=conf,
            sub_type=sub_type,
            facets=facets,
            facet_details=facet_details,
            trace=trace,
        )

        # ── [5] Branch ────────────────────────────────────────────────────────
        if intent is Intent.INFORMATIONAL:
            # Requirement (4): no workflow → full-commitment answer from
            # keywords + features + entities + knowledge.
            answer.intent_confidence = 1.0
            await self._answer_branch(rewritten, kb_context, multi_queries, intent, request, answer)
        else:
            scope = sub_type if request.scope_by_sub_type else None
            await self._action_branch(
                rewritten, facets, kb_context, scope,
                request, answer, multi_queries=multi_queries,
            )

        # Merge top-cosine snapshots (captured per _rrf_search call before the
        # RRF score write-back) into supporting_chunks so the chunk that produced
        # retrieval_top_score is always visible in the table.
        # Each entry is a (snapshot, raw_cos) pair where snapshot.score == raw_cos.
        existing_ids = {c.chunk_id for c in answer.supporting_chunks}
        for cid, (snapshot, raw_cos) in sorted(
            self._top_cosine_chunks.items(),
            key=lambda kv: kv[1][1],   # sort by raw_cos descending
            reverse=True,
        ):
            if cid not in existing_ids:
                answer.supporting_chunks.append(snapshot)
                existing_ids.add(cid)

        # Sort all supporting_chunks by score descending so on-topic rescored
        # chunks (composite score) appear before raw-cosine snapshots from
        # unrelated facet/KB searches that happen to have a high raw cosine.
        answer.supporting_chunks.sort(key=lambda c: c.score, reverse=True)

        # recompute retrieval_top_score from the final supporting_chunks so the
        # header badge always matches the highest score visible in the chunk table.
        if answer.supporting_chunks:
            answer.retrieval_top_score = max(
                c.score for c in answer.supporting_chunks
            )
        else:
            answer.retrieval_top_score = self._retrieval_top_score

        return answer

    # ── Summary-file helpers ──────────────────────────────────────────────────

    def _read_summary_file(self, key: str) -> str:
        """
        Read a file from uploads/summary/ by logical key.
        Returns the full body (skipping the 4-line header).
        """
        filename = _SUMMARY_FILES.get(key)
        if not filename:
            return ""
        path = os.path.join(self._summary_dir, filename)
        if not os.path.isfile(path):
            return ""
        try:
            text = open(path, encoding="utf-8").read().strip()
        except OSError:
            return ""
        # Skip: title line, blank, Category/Generated/Source line, "---"
        lines = text.splitlines()
        body_lines = lines[4:] if len(lines) > 4 else lines
        body = "\n".join(body_lines).strip()
        return body

    def _load_facet_examples(self) -> dict[str, str]:
        """
        Load real examples from each summary MD file.
        These are passed verbatim to the LLM during facet extraction so it can
        match terms that actually exist in the knowledge base.
        """
        return {
            "knowledge": self._read_summary_file("knowledge"),
            "keywords":  self._read_summary_file("keywords"),
            "personas":  self._read_summary_file("personas"),
            "features":  self._read_summary_file("features"),
            "entities":  self._read_summary_file("entities"),
        }

    @staticmethod
    def _build_facet_context(kb_context: str, md_examples: dict[str, str]) -> str:
        """
        Assemble a single context string that combines the KB overview with
        labelled example blocks from each category MD file.
        """
        parts: list[str] = []
        if kb_context:
            parts.append(f"=== KNOWLEDGE BASE OVERVIEW ===\n{kb_context}")
        for key, label in (
            ("keywords", "KEYWORD TERMS (exact terms from the KB)"),
            ("personas", "PERSONA ROLES (exact roles from the KB)"),
            ("features", "FEATURE AREAS (exact feature names from the KB)"),
            ("entities", "ENTITIES (exact entity names from the KB)"),
        ):
            body = md_examples.get(key, "")
            if body:
                parts.append(f"=== {label} ===\n{body}")
        return "\n\n".join(parts)

    # ── RAG-Fusion: RRF over multiple query variants ──────────────────────────

    # Intent → preferred block types (used for a light post-fusion bias).
    # Matches the intent labels emitted by ranking.detect_action_intent.
    _INTENT_BLOCK_BIAS: dict[str, frozenset[str]] = {
        "informational": frozenset({
            ChunkCategory.KEYWORDS.value,
            ChunkCategory.ENTITIES.value,
            ChunkCategory.KNOWLEDGE.value,
        }),
        "action": frozenset({
            ChunkCategory.WORKFLOWS.value,
            ChunkCategory.FEATURES.value,
            ChunkCategory.PERSONAS.value,
        }),
    }
    _RRF_K: int = 60   # standard Cormack et al. constant

    async def _rrf_search(
        self,
        queries: list[str],
        top_k: int,
        category: Optional[str] = None,
        categories: Optional[list[str]] = None,
        sub_type: Optional[str] = None,
        score_threshold: float = 0.0,
        intent_label: Optional[str] = None,
        block_bias: float = 0.15,
    ) -> list[RetrievedChunk]:
        """
        RAG-Fusion retrieval over *queries* (multiple reformulations).

        Pipeline
        --------
        1. Run one _semantic_search per query variant **concurrently**.
        2. Apply Reciprocal Rank Fusion across all ranked result lists.
           RRF score(d) = Σ  w_q / (k + rank_q(d))
           where k=60, w_q=1 for all queries.
        3. Apply a light block-type bias so the intent-preferred categories
           (e.g. keywords/entities for a definition) are nudged upward.
        4. Re-sort descending and return the top-k fused chunks.
           **The fused RRF score is written back to chunk.score** so that all
           downstream ranking (rescore_and_rank, rerank_by_facets, the API
           response) sees the fused rank signal rather than the raw cosine of
           whichever single query retrieved the chunk first.

        Falls back gracefully to a single _semantic_search when len(queries)==1.
        """
        if not queries:
            return []

        # ── Step 1: concurrent per-query retrieval ────────────────────────────
        per_query_results: list[list[RetrievedChunk]] = await asyncio.gather(
            *[
                self._semantic_search(
                    q, top_k,
                    category=category,
                    categories=categories,
                    sub_type=sub_type,
                    score_threshold=score_threshold,
                )
                for q in queries
            ]
        )

        # ── Step 2: Reciprocal Rank Fusion ────────────────────────────────────
        rrf_scores: dict[str, float] = defaultdict(float)
        best_cos:   dict[str, float] = {}          # best raw cosine per chunk
        best_chunk: dict[str, RetrievedChunk] = {}

        for ranked in per_query_results:
            for rank, chunk in enumerate(ranked):
                cid = chunk.chunk_id
                rrf_scores[cid] += 1.0 / (self._RRF_K + rank + 1)
                # keep the chunk object and its best raw cosine seen across queries
                raw_cos = float(getattr(chunk, "score", 0.0))
                if cid not in best_chunk or raw_cos > best_cos.get(cid, 0.0):
                    best_chunk[cid] = chunk
                    best_cos[cid]   = raw_cos

        # ── Step 3: intent-aware block bias ───────────────────────────────────
        preferred = self._INTENT_BLOCK_BIAS.get(intent_label or "", frozenset())
        if preferred and block_bias > 0:
            for cid, chunk in best_chunk.items():
                chunk_type = (chunk.metadata or {}).get("chunk_type", "")
                if chunk_type in preferred:
                    rrf_scores[cid] *= (1.0 + block_bias)

        # ── Step 4: sort by fused score, write back to chunk.score, return top_k
        fused = sorted(rrf_scores.items(), key=lambda kv: -kv[1])[:top_k]

        result: list[RetrievedChunk] = []
        for cid, rrf_score in fused:
            if cid not in best_chunk:
                continue
            chunk = best_chunk[cid]
            raw   = best_cos.get(cid, 0.0)

            # Snapshot the chunk with its best raw cosine BEFORE overwriting
            # chunk.score with the RRF value.  This snapshot is stored in
            # _top_cosine_chunks so it is never affected by later mutations
            # (RRF write-back below, rescore_and_rank in _answer_branch).
            existing = self._top_cosine_chunks.get(cid)
            if existing is None or raw > existing[1]:
                try:
                    snapshot = chunk.model_copy(update={"score": raw})
                except Exception:
                    snapshot = chunk
                self._top_cosine_chunks[cid] = (snapshot, raw)

            # Write the fused RRF score back so downstream ranking (rescore_and_rank,
            # rerank_by_facets, the JSON response) uses the fused signal.
            # Preserve the raw cosine in `summary_cos` so rescore_and_rank can still
            # read it for composite scoring calibration.
            try:
                chunk.summary_cos = raw      # type: ignore[attr-defined]
                chunk.score       = rrf_score
            except Exception:
                pass
            result.append(chunk)

        logger.info(
            "rrf_search  queries=%d  candidates=%d  fused_top_k=%d  intent=%s",
            len(queries), len(rrf_scores), len(result), intent_label or "?",
        )
        return result

    # ── Semantic search helper ────────────────────────────────────────────────

    async def _semantic_search(
        self,
        text: str,
        top_k: int,
        category: Optional[str] = None,
        categories: Optional[list[str]] = None,
        sub_type: Optional[str] = None,
        score_threshold: float = 0.0,
    ) -> list[RetrievedChunk]:
        """ANN search with automatic summary→content fallback.

        Strategy (data-source independent — no topic-specific logic):
          1. Search the summary_embedding index first (default).
          2. If the top summary-cosine is below CONTENT_FALLBACK_THRESHOLD,
             also search the content (raw chunk text) embedding index.
          3. Merge both result sets: for any chunk that appears in both, keep
             the higher of the two scores.  Re-sort descending and return top_k.

        This means a chunk whose summary is poorly worded still surfaces if its
        raw content is a strong match — without forcing the caller to know which
        field will win for a given query.
        """
        settings = get_settings()
        fallback_threshold = getattr(settings, "content_fallback_threshold", 0.85)

        vector      = self._embedder.embed_query(text)
        filter_expr = self._build_filter(category, categories, sub_type)

        # ── Pass 1: summary embedding ─────────────────────────────────────────
        summary_hits = await self._vdb.search(
            query_vector=vector,
            top_k=top_k,
            filter_expr=filter_expr,
            score_threshold=score_threshold,
            anns_field="summary_embedding",
        )

        top_summary_score = summary_hits[0].score if summary_hits else 0.0

        # ── Pass 2: content embedding fallback ───────────────────────────────
        # Only triggered when the best summary score is below the threshold.
        # When summary search is strong (≥ threshold) content search is skipped
        # entirely — no extra Milvus round-trip.
        content_hits: list[RetrievedChunk] = []
        if top_summary_score < fallback_threshold:
            logger.info(
                "semantic_search  summary_top=%.4f < threshold=%.2f"
                " → falling back to content embedding  query=%r",
                top_summary_score, fallback_threshold, text[:80],
            )
            content_hits = await self._vdb.search(
                query_vector=vector,
                top_k=top_k,
                filter_expr=filter_expr,
                score_threshold=score_threshold,
                anns_field="embedding",
            )

        # ── Merge: keep best score per chunk_id, re-sort ─────────────────────
        best: dict[str, RetrievedChunk] = {}
        for hit in summary_hits:
            best[hit.chunk_id] = hit
        for hit in content_hits:
            existing = best.get(hit.chunk_id)
            if existing is None or hit.score > existing.score:
                best[hit.chunk_id] = hit   # content scored higher for this chunk

        hits = sorted(best.values(), key=lambda c: c.score, reverse=True)[:top_k]

        if hits:
            scores = [h.score for h in hits]
            if scores[0] > self._retrieval_top_score:
                self._retrieval_top_score = scores[0]
            # Snapshot tracking is handled in _rrf_search (step 4) where the
            # raw cosine is known and chunk.score has not yet been overwritten.
            # For direct _semantic_search calls (e.g. _kb_vector_context) that
            # bypass _rrf_search, record the top chunk here as a fallback.
            for hit in hits:
                cid     = hit.chunk_id
                raw_cos = float(hit.score)
                existing = self._top_cosine_chunks.get(cid)
                if existing is None or raw_cos > existing[1]:
                    try:
                        snapshot = hit.model_copy(update={"score": raw_cos})
                    except Exception:
                        snapshot = hit
                    self._top_cosine_chunks[cid] = (snapshot, raw_cos)
            used = "summary" if not content_hits else "summary+content"
            logger.info(
                "semantic_search  query=%r  cat=%s  hits=%d  used=%s"
                "  top=%.4f (%.1f%%)  mean=%.4f (%.1f%%)  min=%.4f (%.1f%%)",
                text[:80],
                category or (categories and ",".join(categories)) or "*",
                len(hits), used,
                scores[0],  scores[0]  * 100,
                sum(scores) / len(scores), sum(scores) / len(scores) * 100,
                scores[-1], scores[-1] * 100,
            )
        else:
            logger.info(
                "semantic_search  query=%r  cat=%s  hits=0",
                text[:80],
                category or (categories and ",".join(categories)) or "*",
            )
        return hits

    @staticmethod
    def _build_filter(
        category: Optional[str],
        categories: Optional[list[str]],
        sub_type: Optional[str],
    ) -> str:
        """Compose a Milvus boolean filter from category + sub_type constraints."""
        exprs: list[str] = []
        if category:
            exprs.append(f'chunk_type == "{category}"')
        elif categories:
            joined = ", ".join(f'"{c}"' for c in categories)
            exprs.append(f"chunk_type in [{joined}]")
        if sub_type:
            exprs.append(f'sub_type == "{sub_type}"')
        return " && ".join(exprs)

    async def _kb_vector_context(self, query: str, k: int = 4) -> str:
        """Top KNOWLEDGE chunks as grounding context (vector ANN)."""
        hits = await self._semantic_search(query, k, ChunkCategory.KNOWLEDGE.value)
        blocks = []
        for h in hits:
            label = ranking.facet_label(h)
            body  = (h.content or "").strip().replace("\n", " ")[:300]
            blocks.append(f"[{label}] {body}")
        return "\n".join(blocks)

    # ── [2] Facet extraction ──────────────────────────────────────────────────

    async def _extract_facets(
        self,
        query: str,
        facet_context: str,
        request: AgenticQueryRequest,
    ) -> Facets:
        # Try LLM extraction enriched with real MD examples
        if request.use_llm:
            llm_facets = self._llm.extract_facets(query, facet_context)
            if llm_facets:
                return Facets(
                    keywords=ranking.dedupe_facets(llm_facets["keywords"]),
                    personas=ranking.dedupe_facets(llm_facets["personas"]),
                    features=ranking.dedupe_facets(llm_facets["features"]),
                    entities=ranking.dedupe_facets(llm_facets.get("entities", [])),
                )
        # Fallback: mine facets via semantic search per category
        facets = Facets()
        for name, cat in _FACET_CATEGORIES.items():
            hits   = await self._semantic_search(query, request.facet_top_k, cat)
            labels = ranking.dedupe_facets([ranking.facet_label(h) for h in hits])
            setattr(facets, name, labels)
        return facets

    # ── [3] Fetch facet details (RRF + BFS breadth) ───────────────────────────

    async def _fetch_facet_details(
        self,
        query: str,
        facets: Facets,
        request: AgenticQueryRequest,
        multi_queries: Optional[list[str]] = None,
        intent_label: Optional[str] = None,
    ) -> list[FacetDetail]:
        queries = multi_queries or [query]
        details: list[FacetDetail] = []
        for name, cat in _FACET_CATEGORIES.items():
            values = getattr(facets, name)
            hits   = await self._rrf_search(
                queries, request.facet_top_k,
                category=cat,
                intent_label=intent_label,
            )
            chunks = list(hits)
            if request.traversal in (TraversalStrategy.BFS, TraversalStrategy.BOTH) and hits:
                neigh = await self._graph.bfs_neighborhood(
                    seed_ids=[h.chunk_id for h in hits],
                    hops=request.bfs_hops,
                    max_nodes=request.max_traversal_nodes,
                )
                chunks = self._merge_unique(chunks, neigh)
            details.append(FacetDetail(facet_type=name, values=values, chunks=chunks))
        return details

    # ── [3b] Sub-type-scoped fetch (requirement 3) ────────────────────────────

    async def _fetch_sub_type_scoped(
        self,
        query: str,
        sub_type: str,
        request: AgenticQueryRequest,
        multi_queries: Optional[list[str]] = None,
    ) -> list[FacetDetail]:
        """
        Fetch personas + features + workflows filtered to a single lifecycle
        sub-type (e.g. ``configure``).

        Uses RRF over all multi_queries (when provided) so each category
        benefits from the full set of query reformulations, not just the
        single rewritten query.
        """
        scoped_cats = {
            "personas":  ChunkCategory.PERSONAS.value,
            "features":  ChunkCategory.FEATURES.value,
            "workflows": ChunkCategory.WORKFLOWS.value,
        }
        queries = multi_queries or [query]
        details: list[FacetDetail] = []
        for name, cat in scoped_cats.items():
            hits = await self._rrf_search(
                queries, request.facet_top_k,
                category=cat, sub_type=sub_type,
                intent_label="action",
            )
            details.append(FacetDetail(
                facet_type=f"{name}:{sub_type}",
                values=[sub_type],
                chunks=list(hits),
            ))
        return details

    # ── [5a] Informational branch — answer from information ───────────────────

    async def _answer_branch(
        self,
        query: str,
        kb_context: str,
        multi_queries: list[str],
        intent: Intent,
        request: AgenticQueryRequest,
        answer: AgenticAnswer,
    ) -> None:
        answer.trace.append(
            "branch: INFORMATIONAL → RAG-Fusion answer from keywords/features/entities/knowledge"
        )
        hits = await self._rrf_search(
            multi_queries, request.top_k,
            categories=_INFORMATIONAL_CATS,          # exclude workflows (requirement 4)
            score_threshold=request.score_threshold,
            intent_label=intent.value,
        )
        context_nodes: list[RetrievedChunk] = list(hits)

        for hit in hits:
            if request.traversal in (TraversalStrategy.DFS, TraversalStrategy.BOTH):
                for child_id in hit.children_ids:
                    sub = await self._graph.dfs(child_id, max_nodes=request.dfs_max_nodes)
                    hit.descendants = self._merge_unique(hit.descendants, sub)
                    context_nodes   = self._merge_unique(context_nodes, sub)
                anc = await self._graph.ancestors(hit.chunk_id)
                hit.ancestors = anc
                context_nodes = self._merge_unique(context_nodes, anc)
            if request.traversal in (TraversalStrategy.BFS, TraversalStrategy.BOTH):
                neigh = await self._graph.bfs_neighborhood(
                    [hit.chunk_id], hops=request.bfs_hops,
                    max_nodes=request.max_traversal_nodes,
                )
                context_nodes = self._merge_unique(context_nodes, neigh)

        # Merge facet-detail chunks so the LLM has the full picture
        for fd in answer.facet_details:
            context_nodes = self._merge_unique(context_nodes, fd.chunks)
        context_nodes = context_nodes[: request.max_traversal_nodes]

        # Re-score with IDF-weighted composite + topic-centrality ranking.
        # This is the call site where df/n_docs are populated over the actual
        # candidate set — previously rescore_and_rank was defined but never
        # called, so IDF was always inert (every term scored log(4) ≈ 1.386).
        context_nodes = ranking.rescore_and_rank(query, context_nodes)

        # Build context text: KNOWLEDGE.md grounding + chunk content + facet blocks
        # Strategy: use the summary (which was matched by embedding) to orient the
        # LLM, then append the full verbatim content so the LLM answers from source
        # text — not from the condensed summary alone.
        # Strip internal window-NNN identifiers and Evidence: metadata lines from
        # content before sending to the LLM so they never appear in the answer.
        import re as _re
        _WIN_RE   = _re.compile(r"\bwindow-\d+\b", _re.IGNORECASE)
        _EV_RE    = _re.compile(r"-\s*Evidence:[^\n]*", _re.IGNORECASE)
        _CLEAN_RE = _re.compile(r"\*\*window-\d+\*\*\s*\n?", _re.IGNORECASE)
        # Strip markdown-table junk lines: lines that are only |-, |+, |- -, | ---
        _TBL_JUNK_RE = _re.compile(r"^\s*\|[\s\-\+\|]*$", _re.MULTILINE)
        # Strip entire "## window-NNN" heading lines from answers
        _WIN_HDG_RE  = _re.compile(r"^#{1,4}\s+window-\d+[^\n]*\n?", _re.IGNORECASE | _re.MULTILINE)
        # Strip "Based on the context provided[, ...]" preamble from LLM answers
        _PREAMBLE_RE = _re.compile(
            r"^Based on (?:the )?(?:context|information|provided context)[^,\n]*[,\.]?\s*",
            _re.IGNORECASE,
        )

        def _clean(text: str) -> str:
            t = _WIN_RE.sub("", text)
            t = _EV_RE.sub("", t)
            t = _TBL_JUNK_RE.sub("", t)
            return t.strip()

        def _clean_answer(text: str) -> str:
            """Remove window-NNN labels, headings, and preamble from generated answers."""
            t = _WIN_HDG_RE.sub("", text)
            t = _CLEAN_RE.sub("", t)
            t = _WIN_RE.sub("", t)
            t = _PREAMBLE_RE.sub("", t)
            return t.strip()

        def _chunk_context(n: "RetrievedChunk") -> str:
            """Emit summary (matched by embedding) then full content (answer source)."""
            parts: list[str] = []
            if n.summary:
                parts.append(f"[Summary] {_clean(n.summary)}")
            if n.content:
                parts.append(_clean(n.content))
            return "\n".join(parts)

        kb_section = f"=== KNOWLEDGE BASE ===\n{kb_context[:12000]}\n\n" if kb_context else ""
        main_text = "\n\n".join(
            _chunk_context(n) for n in context_nodes if n.content or n.summary
        )
        facet_blocks: list[str] = []
        for fd in answer.facet_details:
            if fd.chunks:
                lines = "\n".join(
                    f"  - {_clean((c.summary or c.content or '')[:300])}"
                    for c in fd.chunks[:5]
                )
                facet_blocks.append(f"[{fd.facet_type.upper()}]\n{lines}")
        context_text = (
            kb_section
            + main_text
            + ("\n\n" + "\n\n".join(facet_blocks) if facet_blocks else "")
        )

        synthesized = (
            self._llm.synthesize_answer(query, context_text) if request.use_llm else ""
        )
        answer.answer            = _clean_answer(synthesized) or ranking.assemble_answer(query, context_nodes)
        answer.supporting_chunks = hits
        answer.trace.append(
            f"answer assembled from {len(context_nodes)} context chunks "
            f"({'LLM' if synthesized else 'extractive'})"
        )

    # ── [5b] Action branch — workflow → plan ──────────────────────────────────

    async def _action_branch(
        self,
        query: str,
        facets: Facets,
        kb_context: str,
        sub_type: Optional[str],
        request: AgenticQueryRequest,
        answer: AgenticAnswer,
        multi_queries: Optional[list[str]] = None,
    ) -> None:
        answer.trace.append("branch: ACTION → workflow")
        queries = multi_queries or [query]

        # Requirement (3): scope personas + features + workflows to the detected
        # lifecycle sub-type (e.g. "configure").  Use RRF over multi_queries so
        # all reformulations contribute to sub-type-scoped facet retrieval.
        if sub_type:
            answer.trace.append(f"scoping personas/features/workflows by sub_type={sub_type}")
            scoped = await self._fetch_sub_type_scoped(
                query, sub_type, request, multi_queries=queries
            )
            existing = {d.facet_type: d for d in answer.facet_details}
            for fd in scoped:
                if fd.facet_type in existing:
                    existing[fd.facet_type].chunks = self._merge_unique(
                        existing[fd.facet_type].chunks, fd.chunks
                    )
                else:
                    answer.facet_details.append(fd)

        facet_terms = facets.all_terms()

        # Build the facet-augmented workflow query (same as before) and add it
        # as an extra query variant so RRF considers both the bare reformulations
        # AND the facet-enriched form.
        workflows_md   = self._read_summary_file("workflows")
        wf_query_parts = [query]
        if facet_terms:
            wf_query_parts.append(" ".join(facet_terms))
        wf_query = " :: ".join(wf_query_parts)
        answer.trace.append(f"workflow query: {wf_query!r}")

        # Build the full query list for workflow RRF:
        #   multi_queries (original + rewritten + LLM variants)
        #   + facet-augmented wf_query
        #   + optional KB+workflows-md grounding query (for recall)
        wf_queries: list[str] = list(queries)
        if wf_query not in wf_queries:
            wf_queries.append(wf_query)
        if kb_context or workflows_md:
            extra_ctx = (kb_context[:4000] + " " + workflows_md[:4000]).strip()
            ctx_query = (extra_ctx + " " + query).strip()
            wf_queries.append(ctx_query)

        answer.trace.append(
            f"workflow rrf_search  variants={len(wf_queries)}  sub_type={sub_type or '*'}"
        )

        # RRF over all workflow query variants, scoped to sub_type when present.
        wf_hits = await self._rrf_search(
            wf_queries, request.workflow_top_k,
            category=ChunkCategory.WORKFLOWS.value,
            sub_type=sub_type,
            intent_label="action",
        )
        # Fall back to unscoped RRF if sub_type scoping returned nothing.
        if sub_type and not wf_hits:
            answer.trace.append("sub_type-scoped workflow rrf_search empty — retrying unscoped")
            wf_hits = await self._rrf_search(
                wf_queries, request.workflow_top_k,
                category=ChunkCategory.WORKFLOWS.value,
                intent_label="action",
            )

        wf_hits = ranking.rerank_by_facets(wf_hits, facet_terms, boost=request.facet_boost)
        answer.trace.append(f"matched {len(wf_hits)} workflow candidates (facet-boosted RRF)")

        matches: list[WorkflowMatch] = []
        for hit in wf_hits[: request.workflow_top_k]:
            # Fetch workflow via DFS → ordered subtree of steps
            dfs_nodes = await self._graph.dfs(hit.chunk_id, max_nodes=request.dfs_max_nodes)
            steps     = ranking.extract_workflow_steps(dfs_nodes)
            matches.append(WorkflowMatch(
                chunk_id   = hit.chunk_id,
                name       = ranking.facet_label(hit),
                score      = float(getattr(hit, "score", 0.0)),
                base_score = float(getattr(hit, "base_score", getattr(hit, "score", 0.0))),
                steps      = steps,
                chunks     = dfs_nodes,
            ))

        answer.matched_workflows = matches
        if not matches:
            answer.trace.append("no workflows found — cannot build a plan")
            return

        selected = matches[0]
        answer.selected_workflow = selected
        answer.trace.append(
            f"selected workflow: {selected.name!r} ({len(selected.steps)} steps)"
        )

        # ── Whiteboard boxed step: fetch Knowledge + Keywords + Personas +
        # Features + Entities to enrich plan synthesis context.
        # Uses the full multi_queries list (not just [query, wf_query]) so every
        # reformulation contributes to the enrichment context via RRF.
        enrichment_cats = _INFORMATIONAL_CATS + [ChunkCategory.PERSONAS.value]
        enrichment_queries = list(queries)
        if wf_query not in enrichment_queries:
            enrichment_queries.append(wf_query)
        enrichment_hits = await self._rrf_search(
            enrichment_queries,
            request.top_k,
            categories=enrichment_cats,
            intent_label="action",
        )
        answer.trace.append(
            f"action enrichment: {len(enrichment_hits)} chunks "
            f"({'+'.join(c.split('/')[-1] for c in enrichment_cats)})"
        )

        # Build the enriched context block:
        #   1. KB overview (KNOWLEDGE.md)
        #   2. All matched workflow DFS chunks (steps + detail nodes)
        #   3. Knowledge + Keywords + Personas + Features chunks
        #   4. Facet-detail blocks already gathered in step [3]
        import re as _re
        _WIN_RE   = _re.compile(r"\bwindow-\d+\b", _re.IGNORECASE)
        _EV_RE    = _re.compile(r"-\s*Evidence:[^\n]*", _re.IGNORECASE)
        _CLEAN_RE = _re.compile(r"\*\*window-\d+\*\*\s*\n?", _re.IGNORECASE)
        _TBL_JUNK_RE = _re.compile(r"^\s*\|[\s\-\+\|]*$", _re.MULTILINE)
        _WIN_HDG_RE  = _re.compile(r"^#{1,4}\s+window-\d+[^\n]*\n?", _re.IGNORECASE | _re.MULTILINE)
        _PREAMBLE_RE = _re.compile(
            r"^Based on (?:the )?(?:context|information|provided context)[^,\n]*[,\.]?\s*",
            _re.IGNORECASE,
        )

        def _clean(text: str) -> str:
            t = _WIN_RE.sub("", text)
            t = _EV_RE.sub("", t)
            t = _TBL_JUNK_RE.sub("", t)
            return t.strip()

        def _clean_answer(text: str) -> str:
            t = _WIN_HDG_RE.sub("", text)
            t = _CLEAN_RE.sub("", t)
            t = _WIN_RE.sub("", t)
            t = _PREAMBLE_RE.sub("", t)
            return t.strip()

        def _chunk_context(n: "RetrievedChunk") -> str:
            """Emit summary (matched by embedding) then full content (answer source)."""
            parts: list[str] = []
            if n.summary:
                parts.append(f"[Summary] {_clean(n.summary)}")
            if n.content:
                parts.append(_clean(n.content))
            return "\n".join(parts)

        kb_section = f"=== KNOWLEDGE BASE ===\n{kb_context[:8000]}\n\n" if kb_context else ""

        # All DFS nodes from every matched workflow (ordered steps + children)
        all_wf_nodes: list[RetrievedChunk] = []
        for m in matches:
            all_wf_nodes = self._merge_unique(all_wf_nodes, m.chunks)
        wf_section = "\n\n".join(
            _chunk_context(n) for n in all_wf_nodes if n.content or n.summary
        )

        # Enrichment chunks: Knowledge + Keywords + Personas + Features + Entities
        enrich_section = "\n\n".join(
            _chunk_context(n) for n in enrichment_hits if n.content or n.summary
        )

        # Facet blocks (keywords / personas / features / entities detail)
        facet_blocks: list[str] = []
        for fd in answer.facet_details:
            if fd.chunks:
                lines = "\n".join(
                    f"  - {_clean((c.summary or c.content or '')[:300])}"
                    for c in fd.chunks[:5]
                )
                facet_blocks.append(f"[{fd.facet_type.upper()}]\n{lines}")

        # Order: KB overview → enrichment (KB+Keywords+Personas+Features+Entities)
        # → facet blocks → workflow chunks last (may contain low-quality DFS nodes).
        # Putting high-quality enrichment first ensures the LLM grounds in real
        # content even when workflow DFS nodes are sparse or off-topic.
        plan_context = (
            kb_section
            + (f"=== KNOWLEDGE + KEYWORDS + PERSONAS + FEATURES ===\n{enrich_section}\n\n"
               if enrich_section else "")
            + ("\n\n".join(facet_blocks) + "\n\n" if facet_blocks else "")
            + (f"=== WORKFLOW CHUNKS ===\n{wf_section}\n\n" if wf_section else "")
        )

        # Quality gate: if the best matched workflow has fewer than 3 steps its
        # DFS subtree is too sparse to drive a reliable plan.  In that case skip
        # the plan path and synthesise directly from the enriched context (which
        # contains workflow chunks + KB + Keywords + Personas + Features).
        _MIN_STEPS = 3
        steps_are_sufficient = len(selected.steps) >= _MIN_STEPS
        answer.trace.append(
            f"workflow steps: {len(selected.steps)} "
            f"({'sufficient' if steps_are_sufficient else 'sparse — using synthesize_answer'})"
        )

        if steps_are_sufficient:
            # Create plan from workflow steps + enriched context (LLM) or extractive
            llm_plan = (
                self._llm.synthesize_plan(selected.name, selected.steps, context=plan_context)
                if request.use_llm else None
            )
            if llm_plan:
                answer.plan = [
                    PlanStep(
                        order=i + 1,
                        action=p["action"],
                        detail=p.get("detail", ""),
                        source_chunk_id=selected.chunk_id,
                    )
                    for i, p in enumerate(llm_plan)
                ]
                answer.trace.append(f"plan created via LLM ({len(answer.plan)} steps)")
            else:
                source_ids = [c.chunk_id for c in selected.chunks]
                answer.plan = [
                    PlanStep(**p) for p in ranking.build_plan(selected.steps, source_ids)
                ]
                answer.trace.append(
                    f"plan created from DFS steps ({len(answer.plan)} steps)"
                )

            # Format plan as readable prose
            if answer.plan:
                step_lines = "\n".join(
                    f"{p.order}. **{p.action}**" + (f"\n   {p.detail}" if p.detail else "")
                    for p in answer.plan
                )
                # Strip any residual window-NNN identifier from the workflow name so
                # it never appears as a Markdown heading in the final answer.
                import re as _re2
                _safe_name = _re2.sub(r"\bwindow-\d+\b", "", selected.name, flags=_re2.IGNORECASE).strip(" -")
                heading = _safe_name if _safe_name else query[:80]
                answer.answer = f"## {heading}\n\n{step_lines}"

        if not answer.answer:
            # Sparse workflow steps or no plan generated — synthesise the full
            # answer directly from the enriched context (KB + workflow chunks +
            # Keywords + Personas + Features + Entities facets).
            synthesized = (
                self._llm.synthesize_answer(query, plan_context) if request.use_llm else ""
            )
            answer.answer = _clean_answer(synthesized) if synthesized else "\n\n".join(
                c.content.strip() for c in all_wf_nodes[:5] if c.content
            ) or "\n\n".join(
                c.content.strip() for c in enrichment_hits[:5] if c.content
            ) or "_No information could be found for this query._"
            answer.trace.append("answer synthesized from enriched context (LLM)")

        answer.supporting_chunks = enrichment_hits

        # Execute & React — delegated to a downstream executor
        answer.trace.append(
            "execute & react: plan ready — hand off to workflow executor"
        )

    # ── utilities ─────────────────────────────────────────────────────────────

    @staticmethod
    def _merge_unique(
        base: list[RetrievedChunk], extra: list[RetrievedChunk]
    ) -> list[RetrievedChunk]:
        seen = {c.chunk_id for c in base}
        out  = list(base)
        for c in extra:
            if c.chunk_id not in seen:
                seen.add(c.chunk_id)
                out.append(c)
        return out
