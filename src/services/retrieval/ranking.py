"""
Pure ranking / scoring helpers for the agentic retrieval flow.

Everything is a plain function over duck-typed objects — testable without
Milvus, an LLM, or pydantic. Implements the whiteboard's ranking steps:

    detect_action_intent  — "action" vs "informational" heuristic
    rerank_by_facets      — cosine + facet-overlap boost
    extract_workflow_steps — DFS-ordered nodes → ordered step list
    build_plan            — step list → structured plan
    assemble_answer       — extractive LLM-free fallback answer
"""
from __future__ import annotations

import re
from typing import Any

# ── Action-intent vocabulary ──────────────────────────────────────────────────
_ACTION_VERBS = {
    "configure", "config", "set up", "setup", "install", "enable", "disable",
    "deploy", "create", "add", "remove", "delete", "rotate", "revoke", "grant",
    "block", "run", "execute", "start", "stop", "restart", "upgrade", "migrate",
    "connect", "register", "provision", "onboard", "integrate", "schedule",
    "apply", "enforce", "reset", "generate", "build", "import", "export",
    # Additional operational verbs missing from original set:
    "uninstall", "reinstall", "backup", "archive", "restore", "patch",
    "troubleshoot", "diagnose", "monitor", "audit", "report", "verify",
}
_ACTION_PHRASES = (
    "how do i", "how to", "how can i", "steps to", "walk me through",
    "guide me", "set up", "help me set", "i want to", "i need to",
    "can you set", "can you configure", "show me how",
    # Hybrid questions like "What is X and how do I configure it?" should
    # still be detected as action-intent despite starting with "what is".
    "and how do i", "and how to",
)

_STEP_PREFIX_RE = re.compile(
    r"^\s*(?:step\s*\d+|\d+[.)]|[-*•])\s*[:).\-–]*\s*", re.IGNORECASE
)
_WORD_RE = re.compile(r"[A-Za-z0-9_]+")


# ── Intent detection ──────────────────────────────────────────────────────────

def detect_action_intent(query: str) -> tuple[str, float]:
    """
    Heuristic intent classifier → ("action" | "informational", confidence).
    Biases toward 'informational' unless clear action signals appear.
    """
    q = query.lower().strip()
    score = 0.0

    for phrase in _ACTION_PHRASES:
        if phrase in q:
            score += 0.5
            break

    tokens = set(_WORD_RE.findall(q))
    if tokens & {v.replace(" ", "") for v in _ACTION_VERBS}:
        score += 0.4
    for verb in _ACTION_VERBS:
        if " " in verb and verb in q:
            score += 0.4
            break

    # Leading imperative verb is a strong signal
    first = q.split()[0] if q.split() else ""
    if first in _ACTION_VERBS:
        score += 0.3

    # Pure question words → informational
    if q.startswith(("what is", "what are", "why", "when", "who", "which", "define", "explain")):
        score -= 0.4

    score = max(0.0, min(1.0, score))
    return ("action", score) if score >= 0.5 else ("informational", 1.0 - score)


# ── Facet helpers ─────────────────────────────────────────────────────────────

def _node_headings(node: Any) -> list[str]:
    meta = getattr(node, "metadata", None)
    if isinstance(meta, dict):
        h = meta.get("headings") or []
        if h:
            return [str(x) for x in h]
    content = getattr(node, "content", "") or ""
    first = content.strip().splitlines()[0] if content.strip() else ""
    return [first] if first else []


# Matches internal window identifiers that must never appear as user-facing labels.
_WINDOW_ID_RE = re.compile(r"^window-\d+$", re.IGNORECASE)


def facet_label(node: Any, max_len: int = 80) -> str:
    """Best short human label for a chunk: deepest non-window heading, else content head."""
    headings = _node_headings(node)
    # Walk headings from deepest to shallowest, skip bare window-NNN identifiers
    label = ""
    for h in reversed(headings):
        candidate = re.sub(r"\s+", " ", h).strip(" #*-:")
        if candidate and not _WINDOW_ID_RE.match(candidate):
            label = candidate
            break
    if not label:
        content = (getattr(node, "content", "") or "").strip()
        first_line = content.split("\n", 1)[0].strip()
        # Also skip if the first content line is itself a window identifier
        if not _WINDOW_ID_RE.match(first_line):
            label = first_line[:max_len]
    label = re.sub(r"\s+", " ", label).strip(" #*-:")
    return label[:max_len]


def dedupe_facets(labels: list[str]) -> list[str]:
    """Case-insensitive, order-preserving de-dupe of facet strings."""
    seen: set[str] = set()
    out: list[str] = []
    for lbl in labels:
        key = lbl.lower().strip()
        if key and key not in seen:
            seen.add(key)
            out.append(lbl.strip())
    return out


# ── Facet-boosted re-ranking ──────────────────────────────────────────────────

def _term_set(text: str) -> set[str]:
    return {t.lower() for t in _WORD_RE.findall(text) if len(t) > 2}


def rerank_by_facets(
    hits: list[Any],
    facet_terms: list[str],
    boost: float = 0.15,
) -> list[Any]:
    """
    Re-rank ANN hits by:  final = cosine_score + boost × facet_overlap_fraction.
    Facet overlap = fraction of extracted facet terms present in the chunk content.
    Implements the whiteboard's "top-K matching workflows + KB + Keywords + Personas + Features" boost.
    """
    if not facet_terms:
        return sorted(hits, key=lambda h: getattr(h, "score", 0.0), reverse=True)

    wanted: set[str] = set()
    for term in facet_terms:
        wanted |= _term_set(term)
    if not wanted:
        return sorted(hits, key=lambda h: getattr(h, "score", 0.0), reverse=True)

    scored: list[tuple[float, Any]] = []
    for h in hits:
        present = _term_set(getattr(h, "content", "") or "")
        overlap = len(wanted & present) / len(wanted)
        base = float(getattr(h, "score", 0.0))
        final = base + boost * overlap
        try:
            h.base_score = base      # type: ignore[attr-defined]
            h.score = final          # type: ignore[attr-defined]
        except Exception:
            pass
        scored.append((final, h))

    scored.sort(key=lambda t: t[0], reverse=True)
    return [h for _, h in scored]


# ── Workflow step extraction ───────────────────────────────────────────────────

def extract_workflow_steps(dfs_nodes: list[Any], max_steps: int = 30) -> list[str]:
    """
    Turn a DFS-ordered workflow subtree into an ordered list of step strings.
    Handles explicit "Step N:" / numbered / bulleted lists; falls back to
    whole-leaf content when no markup is present.
    """
    steps: list[str] = []
    for node in dfs_nodes:
        content = (getattr(node, "content", "") or "").strip()
        if not content:
            continue
        lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
        step_lines = [ln for ln in lines if _STEP_PREFIX_RE.match(ln)]
        if step_lines:
            for ln in step_lines:
                cleaned = _STEP_PREFIX_RE.sub("", ln).strip()
                if cleaned:
                    steps.append(cleaned)
        else:
            is_leaf = getattr(node, "is_leaf", True)
            if is_leaf:
                snippet = re.sub(r"\s+", " ", content)[:240].strip()
                if snippet:
                    steps.append(snippet)
        if len(steps) >= max_steps:
            break
    return dedupe_facets(steps)[:max_steps]


def build_plan(steps: list[str], source_ids: list[str] | None = None) -> list[dict]:
    """Convert ordered step strings into a structured plan list."""
    source_ids = source_ids or []
    plan: list[dict] = []
    for i, step in enumerate(steps, start=1):
        head = re.split(r"\s[-–:]\s|[.:]\s|\s[-–]\s", step, maxsplit=1)[0].strip()
        action = (head[:70] + "…") if len(head) > 70 else head
        plan.append({
            "order": i,
            "action": action or f"Step {i}",
            "detail": step,
            "source_chunk_id": source_ids[i - 1] if i - 1 < len(source_ids) else "",
        })
    return plan


# ── Extractive answer (LLM-free fallback) ─────────────────────────────────────

def assemble_answer(query: str, context_nodes: list[Any], max_chars: int = 1200) -> str:
    """
    Extractive fallback: stitch the most relevant chunk bodies into a grounded
    response. Used when LLM is disabled or unavailable.
    """
    parts: list[str] = []
    used = 0
    for node in context_nodes:
        body = re.sub(r"\s+", " ", (getattr(node, "content", "") or "")).strip()
        if not body:
            continue
        piece = body
        if used + len(piece) > max_chars:
            piece = piece[: max(0, max_chars - used)]
        parts.append(piece)
        used += len(piece)
        if used >= max_chars:
            break
    if not parts:
        return "No relevant information was found in the knowledge base for this query."
    return " ".join(parts)


# ═══════════════════════════════════════════════════════════════════════════════
# Composite re-scoring / re-ranking
#
# Milvus returns a raw COSINE. That number is not what should be shown, and not
# what should decide the order:
#
#   • DISPLAY  -> composite_score(): calibrated blend of summary cosine (primary),
#                 content cosine (low weight) and facet overlap.
#   • ORDER    -> rank_score(): adds TOPIC-CENTRALITY and SUB-TYPE AGREEMENT.
#
# Keeping these apart is deliberate. Calibrating a cosine changes the displayed
# value but not the order, so a pretty number on a wrongly-ranked chunk is worse
# than useless. The centrality/sub-type terms are what actually fixed the
# measured failure where "What does S-TAP stand for?" returned a page titled
# "S-TAP is not capturing traffic".
# ═══════════════════════════════════════════════════════════════════════════════

from src.services.retrieval.scoring import (  # noqa: E402
    ChunkFacets,
    composite_score,
    rank_score,
)


def _facets_of(node: Any) -> ChunkFacets:
    """Build the scoring facets from a retrieved chunk / graph node."""
    md = getattr(node, "metadata", None)
    get = (lambda k, d=None: getattr(md, k, d)) if md is not None else (lambda k, d=None: d)
    return ChunkFacets(
        headings=list(_node_headings(node) or []),
        keywords=list(getattr(node, "keywords", None) or get("keywords", []) or []),
        features=list(getattr(node, "features", None) or get("features", []) or []),
        workflows=list(getattr(node, "workflows", None) or get("workflows", []) or []),
        entities=list(getattr(node, "entities", None) or get("entities", []) or []),
        personas=list(getattr(node, "personas", None) or get("personas", []) or []),
        summary=getattr(node, "summary", "") or "",
    )


def build_df(nodes: list[Any]) -> tuple[dict[str, int], int]:
    """
    Document frequencies over the candidate set, so IDF can weight rare terms.

    Ideally this is precomputed over the WHOLE corpus at ingest time; computing it
    over the candidate set is a cheap approximation that still ranks a rare term
    ("S-GATE") far above a common one ("configure").
    """
    from src.services.retrieval.scoring import terms
    df: dict[str, int] = {}
    for n in nodes:
        f = _facets_of(n)
        blob = " ".join(f.headings) + " " + f.summary + " " + " ".join(f.keywords)
        for t in terms(blob):
            df[t] = df.get(t, 0) + 1
    return df, max(len(nodes), 1)


def rescore_and_rank(
    query: str,
    nodes: list[Any],
    settings: Any = None,
    top_k: int | None = None,
) -> list[Any]:
    """
    Re-score every candidate with the composite, re-order with the rank score.

    Each node gets:
        node.score            -> the calibrated composite (what the API returns)
        node.score_breakdown  -> the components, for debugging/inspection
    """
    if not nodes:
        return []

    if settings is None:
        from src.config.settings import get_settings
        settings = get_settings()

    weights = {
        "summary": getattr(settings, "score_w_summary", 0.60),
        "content": getattr(settings, "score_w_content", 0.15),
        "facet":   getattr(settings, "score_w_facet", 0.25),
    }
    floor = getattr(settings, "cos_floor", 0.25)
    ceil  = getattr(settings, "cos_ceil", 0.75)

    df, n_docs = build_df(nodes)

    scored = []
    for n in nodes:
        facets = _facets_of(n)
        # summary_cos is the raw ANN cosine written by _rrf_search before the
        # RRF rank score overwrites chunk.score.  If summary_cos is unset or is
        # a tiny RRF-range value (< 0.1) it means the field was never populated
        # — fall back to chunk.score which may itself be the raw cosine (for
        # top-cosine snapshots appended by run()).
        raw_summary = float(getattr(n, "summary_cos", 0.0) or 0.0)
        raw_score   = float(getattr(n, "score", 0.0) or 0.0)
        s_cos = raw_summary if raw_summary >= 0.1 else raw_score
        c_cos = float(getattr(n, "content_cos", None) or 0.0)
        sub   = getattr(getattr(n, "metadata", None), "sub_type", None)

        br = composite_score(query, s_cos, c_cos, facets,
                             weights=weights, df=df, n_docs=n_docs,
                             floor=floor, ceil=ceil)
        r = rank_score(query, s_cos, facets, chunk_sub_type=sub, df=df, n_docs=n_docs)

        try:
            n.score = br.score
            n.score_breakdown = br.as_dict()
        except Exception:                       # frozen/pydantic models
            pass
        scored.append((r, n))

    scored.sort(key=lambda t: t[0], reverse=True)
    out = [n for _, n in scored]
    return out[:top_k] if top_k else out
