"""
Query-understanding layer — LLM-assisted rewrite, facet extraction, answer synthesis.

Every method has a deterministic heuristic fallback so the pipeline runs fully
offline when LLM_ENABLED=false or the AIM endpoint is unreachable.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
from typing import Optional

from src.utils.logging import get_logger

logger = get_logger(__name__)


# ── Product name — read once from the summary files, never hardcoded ──────────

def _read_product_name(fallback: str = "the product") -> str:
    """Return the product name from the first heading line of any summary MD file.

    The summary files carry a title line of the form:
        # Your Product Name — KNOWLEDGE
    This function strips the ``# `` prefix and the `` — <CATEGORY>`` suffix so
    that only the bare product name is returned. Falls back to *fallback* when
    no summary file can be read.
    """
    _SUMMARY_CANDIDATES = [
        "uploads/summary/KNOWLEDGE.md",
        "uploads/summary/KEYWORDS.md",
        "uploads/summary/FEATURES.md",
        "uploads/summary/WORKFLOWS.md",
        "uploads/summary/ENTITIES.md",
        "uploads/summary/PERSONAS.md",
    ]
    for path in _SUMMARY_CANDIDATES:
        try:
            with open(path, encoding="utf-8") as fh:
                first = fh.readline().strip()
            if first.startswith("# "):
                # Strip "# " prefix, then drop " — <CATEGORY>" suffix if present
                name = first[2:].strip()
                name = re.sub(r"\s*—\s*\w+\s*$", "", name).strip()
                if name:
                    return name
        except OSError:
            continue
    return fallback


# Resolved once at module import time.  All prompt strings reference this variable
# so the product name never needs to be hardcoded in prompt text.
_PRODUCT = _read_product_name()


# ── System prompts ─────────────────────────────────────────────────────────────
_REWRITE_SYSTEM = (
    "You rewrite a user's question into a single, specific search query for a "
    "technical knowledge base. "
    "Use the provided KNOWLEDGE BASE and ENTITIES sections to disambiguate "
    "terminology, expand acronyms, and add entity context "
    "(e.g. component names, persona roles). "
    "Preserve hyphenated acronyms exactly as they appear in the knowledge base "
    "(e.g. do not remove hyphens from tokens like S-TAP, S-GATE, K-TAP). "
    "CRITICAL — preserve the question TYPE. "
    "If the question starts with 'what is', 'what are', 'define', 'explain', "
    "'who is', 'describe', keep those words in the rewritten query — they tell "
    "the search engine the user wants a DEFINITION, not a procedure or reference. "
    "Example: 'what is s-tap?' → 'what is S-TAP software tap agent' (NOT 's-tap'). "
    "Example: 'how to install s-tap' → 'install S-TAP agent steps' (action preserved). "
    "ROLE NAMES — never substitute, drop, or generalise a role name (auditor, DBA, "
    "accessmgr, admin, security administrator). If the question names a role, that "
    "exact role name MUST appear in the rewritten query. "
    "Example: 'what can an auditor do that a DBA cannot' → "
    "'auditor vs DBA permissions capabilities Guardium' (NOT 'administrator role'). "
    "TECHNICAL KEYWORDS — preserve exact request keywords: 'syntax', 'full list', "
    "'every', 'all commands', 'step-by-step'. Never replace them with paraphrases. "
    "Example: 'list the full syntax of every grdapi command' → "
    "'full syntax every grdapi command reference list'. "
    "ENUMERATION INTENT — when the user asks to list, enumerate, or see ALL items "
    "(e.g. 'all supported databases', 'list all db', 'what databases are supported', "
    "'can you list all the db'), the rewritten query MUST keep 'all supported' or "
    "'list all' so the retriever knows a complete enumeration is expected. "
    "Do NOT strip 'all', 'supported', 'list', or 'what are' from such queries. "
    "Example: 'What are supported db, can you list all the db' → "
    "'what are all supported databases list'. "
    "Never add invented facts. Output ONLY the rewritten query on one line, "
    "no quotes, no preamble."
)

# Pronouns with no referent — rewriting these produces a worse query than the
# original because the LLM invents a referent.  Detect them heuristically and
# bypass the LLM rewrite entirely.
_PRONOUN_ONLY_RE = re.compile(
    r"^\s*(?:how\s+do\s+i\s+)?(?:set\s+(?:it|this|that)\s+up"
    r"|configure\s+(?:it|this|that)"
    r"|install\s+(?:it|this|that)"
    r"|use\s+(?:it|this|that)"
    r"|enable\s+(?:it|this|that))\s*\??\s*$",
    re.IGNORECASE,
)

_FACET_SYSTEM = f"""\
You are a facet extractor for a {_PRODUCT} knowledge base.

Given the user's question and the CONTEXT (which includes real terms from the KB),
extract matching search facets and return ONLY compact JSON:
{{"keywords": [...], "personas": [...], "features": [...], "entities": [...]}}

Definitions:
  keywords  = product-specific terms, acronyms, or component names from the KB
              (e.g. "S-TAP", "GIM", "FGAC", "S-GATE", "K-TAP", "CyberArk Vault")
  personas  = user roles implied by the question
              (e.g. "Database Administrator", "Security Administrator", "Compliance Officer")
  features  = product capabilities or feature areas referenced
              (e.g. "Data Source Connectivity", "Threat Detection", "Compliance Reporting")
  entities  = named system objects referenced
              (e.g. "collector", "policy", "S-TAP agent", "central manager", "datasource")

Rules:
- Match terms from the CONTEXT examples when possible — do not invent new ones.
- Use [] for any empty category.
- Return ONLY the JSON object. No prose, no markdown, no explanation.
"""

_ANSWER_SYSTEM = (
    f"You are an expert {_PRODUCT} technical consultant. "
    "Your job is to give a thorough, structured, and immediately useful answer "
    "using ALL relevant information found in the CONTEXT sections below.\n\n"
    "Elaboration rules:\n"
    "- E1 Cover the FULL scope of what the context provides: purpose, architecture, "
    "configuration, prerequisites, every step, all options, restrictions, and related "
    "concepts. A thin answer that omits available detail is a failure.\n"
    "- E2 When the context contains steps or procedures, reproduce EVERY step in full "
    "with all its detail — exact UI paths, CLI syntax, field names, parameter values, "
    "and caveats. Never summarise steps into vague phrases.\n"
    "- E3 When multiple context chunks add complementary information about the same "
    "topic, INTEGRATE them into one cohesive explanation. Do not leave any relevant "
    "chunk unused.\n"
    "- E4 When the context mentions specific numeric values, thresholds, UI paths, "
    "field names, commands, flags, or parameters, include them verbatim.\n"
    "- E5 Say each distinct fact ONCE. Do not repeat or paraphrase information you "
    "have already stated.\n\n"
    "Structure rules:\n"
    "- Start with a concise direct answer (1–3 sentences) — no preamble phrases.\n"
    "- Follow with clearly labelled sections using descriptive ## headings that "
    "name the actual topic (e.g., ## How S-TAP Intercepts Traffic, "
    "## Configuration Steps, ## Prerequisites) — NEVER use ## to introduce a "
    "bare heading like '## Overview' alone, and NEVER use window references or "
    "chunk identifiers as headings.\n"
    "- Use a numbered list for ordered steps or procedures. "
    "Number items sequentially (1, 2, 3 …) in a SINGLE continuous list — "
    "never restart numbering mid-procedure. "
    "If a step has sub-details, indent them as bullet points under that step "
    "(do NOT insert a new numbered list). "
    "Example of correct format:\n"
    "  1. First step\n"
    "     - sub-detail A\n"
    "     - sub-detail B\n"
    "  2. Second step\n"
    "  3. Third step\n"
    "- Use bullet points for properties, modes, options, or unordered items. "
    "Every bullet MUST be a complete phrase or sentence.\n"
    "- Use a table when comparing multiple options or attributes.\n"
    "- Use inline code formatting for UI field names, commands, or config values.\n\n"
    "Content cleanliness rules (STRICT):\n"
    "- NEVER start any line, bullet, step, or heading with '|- ', '|+ ', '| ', "
    "'###', '####', or any markdown table separator character. "
    "These are source artefacts — strip them entirely.\n"
    "- Every sentence, bullet, step, and heading MUST begin with a letter or digit. "
    "If stripping a prefix leaves a bare fragment, complete the sentence or omit it.\n"
    "- NEVER emit a line that is only punctuation, pipe characters, or whitespace.\n\n"
    "Grounding rules:\n"
    "- Ground every statement in the provided context — never invent facts.\n"
    "- NEVER start the answer with 'Based on the context provided', "
    "'Based on the information provided', 'Based on the provided context', "
    "or any similar preamble. Begin directly with the answer.\n"
    "- Do NOT include chunk IDs, UUIDs, or any identifier matching 'window-NNN' "
    "(e.g. window-19, window-203). These are internal system labels.\n"
    "- Do NOT include Evidence: strings or ':: category' metadata.\n"
    "- Do NOT include bare markdown table separators such as '|-', '|+', '|- -', "
    "or lines that consist only of '|' characters. If the source contains a table, "
    "render it as a proper markdown table or convert it to bullet points.\n"
    "- If the context is insufficient, state what IS known, then note the gap "
    "in one sentence.\n"
    "- Output ONLY the answer, no preamble."
)

_MULTI_QUERY_SYSTEM = (
    "You are a query diversification engine for a technical knowledge base. "
    "Given a primary search query, generate exactly 4 alternative phrasings that "
    "together maximise retrieval recall by covering orthogonal angles.\n\n"
    "Angle coverage (use all four):\n"
    "  1. SYNONYM / PARAPHRASE — same intent, different vocabulary or acronym expansion "
    "(e.g. 'S-TAP' → 'Software TAP agent', 'GIM' → 'Guardium Installation Manager').\n"
    "  2. CONCEPT / DEFINITION — what the thing IS, its purpose, or its architecture "
    "(good for chunks that define rather than instruct).\n"
    "  3. PROCEDURE / TASK — how to do it, configure it, or troubleshoot it "
    "(imperative phrasing; good for workflow/feature chunks).\n"
    "  4. ENTITY / RELATION — name the components, roles, or systems involved and how "
    "they relate (good for entity/persona chunks).\n\n"
    "Rules:\n"
    "- Each variant must be a standalone search query (no pronouns referring to others).\n"
    "- Do NOT repeat the primary query verbatim.\n"
    "- Do NOT invent facts or hallucinate component names.\n"
    "- Preserve hyphenated identifiers exactly (S-TAP, K-TAP, A-TAP, S-GATE, GIM, CAS).\n"
    "- Output ONLY the 4 variants, one per line, no numbering, no bullets, no preamble."
)

_PLAN_SYSTEM = (
    f"You are an expert {_PRODUCT} technical consultant. "
    "Your job is to produce a precise, step-by-step execution plan that directly "
    "answers the user's question.\n\n"
    "You are given:\n"
    "  WORKFLOW STEPS — the ordered procedure extracted from the knowledge base.\n"
    "  CONTEXT — supporting chunks: Knowledge Base overview, Keywords, Personas, "
    "Features, and Entities relevant to this task.\n\n"
    "Rules:\n"
    "- Ground every step in the WORKFLOW STEPS and CONTEXT. Do not invent actions.\n"
    "- Expand each step with concrete detail drawn from CONTEXT: exact UI paths, "
    "CLI commands, field names, parameter values, prerequisites, or caveats.\n"
    "- Preserve the original execution order from WORKFLOW STEPS.\n"
    "- If CONTEXT reveals prerequisites or post-steps not in WORKFLOW STEPS, "
    "include them as the first/last steps respectively.\n"
    "- Return ONLY valid JSON: "
    '{"plan": [{"action": "...", "detail": "..."}, ...]} '
    "No prose, no markdown, no explanation outside the JSON."
)


class QueryUnderstanding:
    def __init__(self, settings=None, provider=None):
        if settings is None:
            from src.config.settings import get_settings
            settings = get_settings()
        self._settings = settings
        self._enabled  = bool(getattr(settings, "llm_enabled", False))
        self._provider = provider
        if self._enabled and self._provider is None:
            self._provider = self._build_aim(settings)
        logger.info("QueryUnderstanding  llm_enabled=%s", self.enabled)

    @staticmethod
    def _build_aim(settings):
        try:
            return _AIMChat(
                base_url   = settings.llm_base_url,
                api_key    = settings.llm_api_key,
                model      = settings.llm_model,
                max_tokens = getattr(settings, "llm_max_output_tokens", 4000),
                timeout    = getattr(settings, "llm_timeout", 120),
            )
        except Exception as exc:
            logger.warning("AIM init failed (%s) — LLM steps disabled", exc)
            return None

    @property
    def enabled(self) -> bool:
        return self._enabled and self._provider is not None

    def _complete(self, system: str, user: str) -> str:
        if not self.enabled:
            return ""
        try:
            return self._provider.complete(system, user).strip()
        except Exception as exc:
            logger.warning("LLM completion failed: %s", exc)
            return ""

    # ── 1. Rewrite with Knowledge Base + entity context ───────────────────────

    def rewrite_query(self, query: str, kb_context: str) -> str:
        """
        Rewrite the user query using KB context (KNOWLEDGE.md + top KNOWLEDGE chunks)
        for better retrieval. Expands acronyms and adds entity names.

        Pronoun-only queries (e.g. "How do I set it up?") are returned unchanged:
        the LLM would invent a referent, producing a worse embed vector than the
        original two-word query.
        """
        if _PRONOUN_ONLY_RE.match(query):
            logger.info("rewrite_query: pronoun-only query detected — returning unchanged: %r", query)
            return query

        out = self._complete(
            _REWRITE_SYSTEM,
            f"KNOWLEDGE BASE:\n{kb_context}\n\nQUESTION:\n{query}\n\nRewritten query:",
        )
        rewritten = out.splitlines()[0].strip() if out else ""
        if rewritten and 3 <= len(rewritten) <= 400:
            return rewritten
        return query    # heuristic fallback

    # ── 1b. Multi-query generation ────────────────────────────────────────────

    def generate_multi_queries(self, primary: str) -> list[str]:
        """
        Return a list of up to 5 queries: the primary plus 4 LLM-generated
        variants covering different retrieval angles (synonyms, acronym
        expansions, perspective shifts, related sub-topics).

        Falls back to [primary] when LLM is disabled or the call fails.
        """
        out = self._complete(
            _MULTI_QUERY_SYSTEM,
            f"PRIMARY QUERY:\n{primary}\n\nAlternative queries:",
        )
        if not out:
            return [primary]
        variants = [
            line.strip().lstrip("-•*0123456789.) ")
            for line in out.splitlines()
            if line.strip()
        ]
        # Keep only non-empty, non-duplicate variants (up to 4)
        seen: set[str] = {primary.lower()}
        deduped: list[str] = []
        for v in variants:
            if v and v.lower() not in seen and 3 <= len(v) <= 400:
                seen.add(v.lower())
                deduped.append(v)
            if len(deduped) == 4:
                break
        return [primary] + deduped

    # ── 2. Extract Keywords / Personas / Features (with MD examples) ──────────

    def extract_facets(self, query: str, kb_context: str) -> Optional[dict]:
        """
        Returns {'keywords':[], 'personas':[], 'features':[]} or None.

        kb_context should include the full MD example blocks so the LLM can
        match real terms from the knowledge base.
        """
        out = self._complete(
            _FACET_SYSTEM,
            f"CONTEXT (real terms from the knowledge base):\n{kb_context[:16000]}"
            f"\n\nQUESTION:\n{query}\n\nJSON:",
        )
        parsed = _safe_json(out)
        if isinstance(parsed, dict) and any(
            k in parsed for k in ("keywords", "personas", "features", "entities")
        ):
            return {
                "keywords": _as_str_list(parsed.get("keywords")),
                "personas": _as_str_list(parsed.get("personas")),
                "features": _as_str_list(parsed.get("features")),
                "entities": _as_str_list(parsed.get("entities")),
            }
        return None

    # ── 5a. Synthesised answer (informational branch) ─────────────────────────

    def synthesize_answer(self, query: str, context: str) -> str:
        return self._complete(
            _ANSWER_SYSTEM,
            f"CONTEXT:\n{context[:432000]}\n\nQUESTION:\n{query}\n\nAnswer:",
        )

    # ── 5b. Plan narrative (action branch) ────────────────────────────────────

    def synthesize_plan(
        self,
        workflow_name: str,
        steps: list[str],
        context: str = "",
    ) -> Optional[list[dict]]:
        """
        Build a structured plan from workflow steps enriched with supporting context.

        context should contain Knowledge + Keywords + Personas + Features + Entities
        chunks assembled by _action_branch (the whiteboard's boxed step:
        "top-K matching workflows + Knowledge + Keywords + Personas + Features").
        """
        joined = "\n".join(f"- {s}" for s in steps)
        user_parts = [f"WORKFLOW: {workflow_name}", f"WORKFLOW STEPS:\n{joined}"]
        if context:
            user_parts.append(f"CONTEXT:\n{context[:28000]}")
        user_parts.append("JSON:")
        out = self._complete(_PLAN_SYSTEM, "\n\n".join(user_parts))
        parsed = _safe_json(out)
        if isinstance(parsed, dict) and isinstance(parsed.get("plan"), list):
            plan = []
            for item in parsed["plan"]:
                if isinstance(item, dict):
                    plan.append({
                        "action": str(item.get("action", "")).strip(),
                        "detail": str(item.get("detail", "")).strip(),
                    })
            if plan:
                return plan
        return None


# ── helpers ───────────────────────────────────────────────────────────────────

def _safe_json(text: str):
    if not text:
        return None
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()
    m = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if m:
        text = m.group(0)
    try:
        return json.loads(text)
    except Exception:
        return None


def _as_str_list(value) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(v).strip() for v in value if str(v).strip()]


class _AIMChat:
    """IBM AIM chat/completions via /usr/bin/curl (avoids Akamai TLS fingerprint block)."""

    def __init__(self, base_url: str, api_key: str, model: str, max_tokens: int, timeout: int):
        self._url        = base_url.rstrip("/") + "/inference/chat/completions"
        self._api_key    = api_key
        self._model      = model
        self._max_tokens = max_tokens
        self._timeout    = timeout

    def complete(self, system: str, user: str) -> str:
        body = json.dumps({
            "model": self._model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user",   "content": user},
            ],
            "max_tokens": self._max_tokens,
        })
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
            tmp.write(body)
            tmp_path = tmp.name
        try:
            result = subprocess.run(
                [
                    "/usr/bin/curl", "-s", "-X", "POST", self._url,
                    "-H", f"Authorization: Bearer {self._api_key}",
                    "-H", "Content-Type: application/json",
                    "-H", "Accept: application/json",
                    "-d", f"@{tmp_path}",
                    "--max-time", str(self._timeout),
                ],
                capture_output=True, text=True, timeout=self._timeout + 5,
            )
        finally:
            os.unlink(tmp_path)
        if result.returncode != 0:
            raise RuntimeError(f"curl failed (rc={result.returncode}): {result.stderr[:200]}")
        raw = result.stdout.strip()
        if raw.lstrip().startswith("<"):
            raise RuntimeError(f"WAF block: {raw[:120]}")
        data = json.loads(raw)
        if "error" in data or "choices" not in data:
            raise RuntimeError(f"AIM error: {raw[:300]}")
        return data["choices"][0]["message"]["content"]
