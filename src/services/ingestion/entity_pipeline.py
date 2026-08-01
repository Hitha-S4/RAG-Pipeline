"""
Entity pipeline — window-based LLM extraction flow.

    PDF
      ↓ 1. extract text                (loader)
      ↓ 2. clean — pass A: rules       (DocumentProcessor: non-ASCII → ASCII, dedup)
      ↓ 3. window-based chunking       (pack text into the LLM's large context window)
      ↓ 4. clean — pass B: LLM         (per window: strip residual page noise, rejoin
      ↓                                 hyphen-split words, fix OCR artefacts → clean markdown)
      ↓ 5. LLM processing              (per cleaned window, ONE pass extracts:)
      ↓      ├─ typed chunks: knowledge | keywords | personas | workflows | features | entities
      ↓      │    (knowledge is the catch-all — anything not fitting another type
      ↓      │     MUST still be emitted as knowledge, so no source data is lost)
      ↓      ├─ sub_type   (install/configure/… lifecycle axis)
      ↓      ├─ relations  (facets linking persona ↔ feature ↔ workflow ↔ entity ↔ keyword)
      ↓      └─ summary    (per extracted entity — created in the SAME pass)
      ↓ 6. recursive chunking          (AFTER all LLM processing: the processed content is
      ↓                                 re-chunked with the recursive strategy — target/ceiling/
      ↓                                 overlap from settings, e.g. 640 tok / 64 overlap —
      ↓                                 so every stored unit fits the embedding model)
      ↓ 7. summaries for new chunks    (SummarizerService: each recursive leaf gets its own
      ↓                                 summary; entity blocks keep their extraction summary)
      ↓ 8. embeddings                  (recursive-chunk/content vector + summary vector)
      ↓ 9. persist
             • Markdown  <CATEGORY>.md   (summaries, grouped by category)
             • JSONL     chunks_<cat>.jsonl (structured output)
             • Milvus    vectors + metadata (14-field schema)

Relations are persisted two ways:
    • facet lists on each chunk (keywords/features/workflows/personas/entities)
    • a tree: each window gets one root knowledge chunk (depth=1); every other
      chunk extracted from that window is its child (depth=2). parent_id /
      children_ids drive the DFS/BFS graph traversal at retrieval time.
"""
from __future__ import annotations

import asyncio
import re
from datetime import datetime, timezone
from pathlib import Path

from src.config.settings import get_settings
from src.services.ingestion.prompts.extraction_v3 import (
    ALL_TYPES_SYSTEM,
    ALL_TYPES_SYSTEM_COMPACT,
    ALL_TYPES_USER,
    DIRECT_USER,
    EXTRACTION_ORDER,
    ROUTER_SYSTEM,
    ROUTER_USER,
    TYPE_PROMPTS,
    TYPED_USER,
    build_domain_profile,
)
from src.enums import ChunkCategory, ChunkSubType, SourceType
from src.models import Chunk, Document
from src.services.ingestion.embedders import EmbeddingService
from src.services.ingestion.llm_service import LLMService
from src.services.ingestion.loaders.loader import get_loader
from src.services.ingestion.output_writer import OutputWriterService
from src.services.ingestion.processors import DocumentProcessor
from src.services.vectordb.milvus_service import MilvusService
from src.utils.logging import get_logger

logger = get_logger(__name__)

_VALID_TYPES = frozenset(e.value for e in ChunkCategory)
_VALID_SUBS  = frozenset(e.value for e in ChunkSubType)


# ── Step 3: window-based chunking ─────────────────────────────────────────────

# Chars-per-token used for window sizing. MUST match _EST_CHARS_PER_TOKEN in
# utils/providers.py — the provider estimates input tokens from body chars with
# this ratio to compute the output budget. If the two disagree, windows look
# small here and huge to the provider, and the output budget collapses.
_EST_CHARS_PER_TOKEN = 3.0


def window_char_budget() -> int:
    """Return the max chars per window, derived from LLM_INPUT_WINDOW_TOKENS.

    CRITICAL: keep LLM_INPUT_WINDOW_TOKENS small (8,000 – 10,000 tokens).
    Larger windows produce FEWER total chunks because the LLM can only attend
    to ~24k chars of content before extraction density collapses.

    The OUTPUT budget (LLM_MAX_OUTPUT_TOKENS) can and should be set higher
    (16,000 – 32,000) so the LLM does not truncate mid-extraction.

    Empirical results (gdp-12.x, 1829 pages):
      8,000 tok input  (24k chars/window) → 241 windows → 4,120 chunks   OK
     32,000 tok input  (96k chars/window) →  13 windows →   132 chunks   BAD (30x regression)
    """
    s       = get_settings()
    win_tok = getattr(s, "llm_input_window_tokens", None) or s.llm_max_tokens
    budget  = int(win_tok * _EST_CHARS_PER_TOKEN)
    logger.debug("window_char_budget: win_tok=%d → %d chars/window", win_tok, budget)
    return budget


def make_windows(text: str, *, overlap_paragraphs: int = 1) -> list[str]:
    """
    FIXED-WINDOW chunking sized to the LLM context — used BEFORE LLM processing.
    (Recursive 640/64 chunking happens AFTER LLM processing, for embedding.)

    Splits at paragraph boundaries where possible; consecutive windows overlap
    by `overlap_paragraphs` so no entity is cut in half at a boundary.

    OVERSIZED PARAGRAPHS ARE NOW HARD-SPLIT.
        This function previously broke ONLY between paragraphs, so a single
        paragraph longer than max_chars became one oversized window and the
        "<= max_chars" contract was silently violated. Observed: a 6,000-char
        budget producing a 15,612-char window (2.6x over). Since generation
        time scales with window size and the gateway kills any request at ~30 s,
        an oversized window is a guaranteed HTTP 504.

        Long paragraphs are split on sentence boundaries where possible, and
        mid-sentence only when a single sentence exceeds the budget on its own
        (long command dumps and tables do this).
    """
    max_chars = window_char_budget()

    def _split_oversized(par: str) -> list[str]:
        """Break one over-budget paragraph into <= max_chars pieces."""
        if len(par) <= max_chars:
            return [par]
        pieces: list[str] = []
        # Prefer sentence ends; fall back to hard slicing for runaway lines.
        sentences = re.split(r"(?<=[.!?])\s+", par)
        cur = ""
        for sent in sentences:
            while len(sent) > max_chars:          # single monster sentence
                if cur:
                    pieces.append(cur)
                    cur = ""
                pieces.append(sent[:max_chars])
                sent = sent[max_chars:]
            if len(cur) + len(sent) + 1 > max_chars and cur:
                pieces.append(cur)
                cur = sent
            else:
                cur = f"{cur} {sent}".strip() if cur else sent
        if cur:
            pieces.append(cur)
        return pieces

    raw_paragraphs = re.split(r"\n\n+", text)
    paragraphs: list[str] = []
    oversized = 0
    for par in raw_paragraphs:
        if len(par) > max_chars:
            oversized += 1
            paragraphs.extend(_split_oversized(par))
        else:
            paragraphs.append(par)
    if oversized:
        logger.info("Windowing: hard-split %d oversized paragraph(s) to fit %d chars",
                    oversized, max_chars)
    windows: list[str] = []
    buf: list[str] = []
    size = 0
    for p in paragraphs:
        p_len = len(p) + 2
        if size + p_len > max_chars and buf:
            windows.append("\n\n".join(buf))
            buf = buf[-overlap_paragraphs:] if overlap_paragraphs else []
            size = sum(len(x) + 2 for x in buf)
            # THE OVERLAP CAN ITSELF BLOW THE BUDGET.
            # After flushing we carry `overlap_paragraphs` paragraphs forward,
            # then unconditionally append the current one. If both are near
            # max_chars the resulting window is ~2x the budget — observed as
            # largest=5983 against a 3000-char budget. Drop the overlap when
            # keeping it would overflow: a lost overlap costs one boundary
            # entity, an oversized window costs the whole request to a gateway
            # timeout.
            if size + p_len > max_chars:
                buf = []
                size = 0
        buf.append(p)
        size += p_len
    if buf:
        windows.append("\n\n".join(buf))
    biggest = max((len(w) for w in windows), default=0)
    logger.info("Windowing: %d chars → %d window(s) (≤%d chars each, largest=%d)",
                len(text), len(windows), max_chars, biggest)
    if biggest > max_chars:
        logger.error(
            "Windowing: largest window is %d chars, %.1fx the %d-char budget. "
            "Oversized windows time out at the gateway — this must not happen.",
            biggest, biggest / max_chars, max_chars,
        )
    return windows


# ── Step 4: LLM cleaning pass (per window) ────────────────────────────────────
#
# NOTE: this pass asks the LLM to reproduce the ENTIRE window text (~60k tokens
# of input) back cleaned.  With LLM_MAX_OUTPUT_TOKENS=4000 the model can only
# emit ~4k tokens — far below the _MIN_KEEP_RATIO threshold — so every window
# falls back to the rule-cleaned original, wasting 22 concurrent LLM calls and
# adding ~2 minutes of latency with zero benefit.
#
# The pass is therefore DISABLED by default (llm_clean_enabled=False in settings).
# DocumentProcessor (step 2) already handles non-ASCII, deduplication, and basic
# normalisation; the extraction prompt is robust to raw PDF text.
#
# To re-enable: set LLM_CLEAN_ENABLED=true in .env AND raise
# LLM_MAX_OUTPUT_TOKENS to at least ceil(max_window_chars / chars_per_token)
# so the model can actually reproduce the full window.

CLEAN_SYSTEM = """\
You are a documentation cleaning engine. You receive one window of text
extracted from a PDF. Return the SAME content, cleaned:

- Remove residual page noise: running headers/footers, bare page numbers,
  table-of-contents lines, "continued on next page" markers, legal boilerplate.
- Rejoin words split by line-break hyphenation ("config- uration" → "configuration")
  and OCR-split words ("Data base" → "Database" ONLY when clearly one word).
- Merge lines broken mid-sentence back into single paragraphs.
- Normalise headings to markdown (#, ##, ###) using the document's own hierarchy.
- Keep tables as markdown tables; keep commands/code exactly as written.

STRICT RULES:
- This is CLEANING, not summarising. Do NOT shorten, paraphrase, reorder,
  or drop any substantive sentence. Every fact in the input must remain.
- Do not add anything that is not in the input.
- Output ONLY the cleaned markdown. No preamble, no commentary, no fences.\
"""

CLEAN_USER = "WINDOW {index} of {total}:\n\n{text}\n\nReturn the cleaned markdown now."

# An LLM cleaning response that lost too much text means it summarised or
# truncated instead of cleaning — fall back to the rule-cleaned window.
_MIN_KEEP_RATIO = 0.55


def llm_clean_windows(llm: LLMService, windows: list[str]) -> list[str]:
    """Pass B cleaning: run every window through the LLM cleaner concurrently.

    Disabled by default — see module-level note above.  Only runs when
    LLM_CLEAN_ENABLED=true in settings AND the LLM is enabled.
    """
    s = get_settings()
    if not getattr(s, "llm_clean_enabled", False):
        logger.debug("LLM cleaning pass disabled (llm_clean_enabled=false) — skipping")
        return windows
    if not llm.enabled:
        logger.warning("LLM disabled — skipping LLM cleaning pass")
        return windows
    reqs = [(CLEAN_SYSTEM, CLEAN_USER.format(index=i + 1, total=len(windows), text=w))
            for i, w in enumerate(windows)]
    responses = llm.complete_batch(reqs)
    cleaned: list[str] = []
    for i, (orig, resp) in enumerate(zip(windows, responses)):
        resp = (resp or "").strip()
        if len(resp) >= len(orig) * _MIN_KEEP_RATIO:
            cleaned.append(resp)
        else:
            logger.warning("LLM clean window %d kept %.0f%% of text — using rule-cleaned original",
                           i + 1, 100 * len(resp) / max(1, len(orig)))
            cleaned.append(orig)
    return cleaned


# ── Step 5: LLM extraction prompt (product-independent) ───────────────────────
# ALL_TYPES_SYSTEM / ALL_TYPES_USER: single call per window that emits all six
# block types in one LLM reply — no router, no per-type passes.
# Domain vocabulary is built once from the cleaned document text and injected
# so the model knows which identifiers to carry verbatim.



_BLOCK_RE = re.compile(r"===\s*(\d+)\s*===")
_FIELD_RE = re.compile(
    r"^-\s*(Type|Categories|SubType|Name|Content|Evidence|Summary|Keywords|Features|Workflows|Personas|Entities)\s*:\s*(.*)$",
    re.IGNORECASE,
)
# Granite (and other models) emit these markers when truncated mid-output.
# Strip them so they don't pollute stored content.
_TRUNCATION_RE = re.compile(
    r"\s*(?:=cut|\.\.\.?\s*\(truncated[^)]*\)|\.\.\.?\s*(?:and so on|etc)\.?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def _clean_field(text: str) -> str:
    """Remove LLM truncation artefacts from a field value."""
    return _TRUNCATION_RE.sub("", text).strip()


def parse_blocks(raw: str) -> list[dict]:
    """Parse ===N=== blocks into record dicts. Tolerant of minor drift."""
    records: list[dict] = []
    parts = _BLOCK_RE.split(raw)
    # parts = [prefix, n1, body1, n2, body2, ...]
    for body in parts[2::2]:
        rec: dict = {"type": "", "sub_type": "", "name": "", "content": "",
                     "summary": "", "keywords": [], "features": [],
                     "workflows": [], "personas": [], "entities": []}
        current: str | None = None
        for line in body.splitlines():
            m = _FIELD_RE.match(line.strip())
            if m:
                key = m.group(1).lower()
                val = m.group(2).strip()
                current = key
                if key in ("keywords", "features", "workflows", "personas", "entities"):
                    items = [x.strip() for x in val.split(",")]
                    rec[key] = [x for x in items if x and x.lower() != "none"]
                elif key == "subtype":
                    rec["sub_type"] = val.lower()
                elif key == "categories":
                    # CLASSIFY_SYSTEM uses "Categories: cat1, cat2, …"
                    # Take the first valid category as the primary type; the rest
                    # are stored in rec["extra_categories"] for multi-label use.
                    cats = [c.strip().lower() for c in val.split(",")
                            if c.strip().lower() in _VALID_TYPES]
                    rec["type"] = cats[0] if cats else "knowledge"
                    rec["extra_categories"] = cats[1:]
                else:
                    rec[key] = val
            elif current == "content":
                # Continue accumulating content lines — including blank lines
                # inside a multi-paragraph verbatim passage. Stop only when
                # the next structured field header starts (handled by _FIELD_RE
                # match above). A blank line here is paragraph separation
                # within the content, not a terminator.
                rec["content"] += "\n" + line.rstrip()
        rec["type"] = rec["type"].lower()
        rec["content"] = _clean_field(rec["content"])
        rec["summary"] = _clean_field(rec["summary"])
        # CLASSIFY_SYSTEM omits Name and Content — accept a block when summary
        # is present even if name/content are empty.
        has_body = rec["content"] or rec["summary"]
        if rec["type"] in _VALID_TYPES and has_body:
            if rec["sub_type"] not in _VALID_SUBS:
                rec["sub_type"] = ChunkSubType.OTHER.value
            records.append(rec)
    return records


def records_to_chunks(records: list[dict], window_index: int) -> list[Chunk]:
    """
    Materialise Chunk objects and build the relation tree for one window:
    root knowledge chunk (depth=1) ← children: every other block (depth=2).
    """
    chunks: list[Chunk] = []
    for rec in records:
        # CLASSIFY_SYSTEM produces no Content/Name fields — fall back to summary.
        content = rec["content"].strip() or rec["summary"]
        name    = rec["name"].strip()    or rec["summary"][:80]
        c = Chunk(
            content=content,
            summary=rec["summary"],
            keywords=rec["keywords"], features=rec["features"],
            workflows=rec["workflows"], personas=rec["personas"],
            entities=rec["entities"],
        )
        c.metadata.chunk_type = ChunkCategory(rec["type"])
        c.metadata.sub_type   = rec["sub_type"]
        c.metadata.headings   = [name, f"window-{window_index}"]
        chunks.append(c)

    # Tree: first knowledge block is the window root; all others are children.
    root = next((c for c in chunks
                 if c.metadata.chunk_type is ChunkCategory.KNOWLEDGE), None)
    if root:
        root.metadata.depth   = 1
        root.metadata.is_leaf = False
        for c in chunks:
            if c is root:
                continue
            c.metadata.depth     = 2
            c.metadata.is_leaf   = True
            c.metadata.parent_id = root.chunk_id
            root.metadata.children_ids.append(c.chunk_id)
    return chunks


# ── Step 6: recursive chunking of the LLM-processed content ──────────────────

def recursive_rechunk(chunks: list[Chunk]) -> list[Chunk]:
    """
    AFTER all LLM processing, re-chunk every entity block whose content exceeds
    the ceiling using the recursive strategy (settings: chunk_target_tokens /
    chunk_ceiling_tokens / chunk_overlap_tokens — e.g. 640 tok, 64 overlap).

    Split pieces become leaf children of the entity block:
        window root (knowledge, depth=1)
          └─ entity block (depth=2, is_leaf=False when split)
               └─ recursive pieces (depth=3, is_leaf=True)

    Pieces inherit chunk_type / sub_type / relations from their parent so
    category- and facet-filtered retrieval still works, and parent_id keeps
    DFS/BFS traversal intact. Blocks already under the ceiling stay as-is.

    Each split leaf inherits the PARENT block's LLM-generated summary verbatim.
    The content is the raw piece of the window text; the summary describes the
    whole block those pieces came from — so all sibling leaves share the same
    summary, and rechunk_and_summarize will not re-summarise them (non-empty
    summary skips the SummarizerService pass).
    """
    from src.services.ingestion.chunkers.splitter import RecursiveCharacterTextSplitter

    s = get_settings()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=s.chunk_target_tokens,
        chunk_overlap=s.chunk_overlap_tokens,
        chars_per_token=s.chars_per_token,
    )
    ceiling_chars = int(s.chunk_ceiling_tokens * s.chars_per_token)

    out: list[Chunk] = []
    n_split = 0
    for c in chunks:
        out.append(c)
        if len(c.content) <= ceiling_chars:
            continue
        pieces = splitter.split_text(c.content)
        if len(pieces) <= 1:
            continue
        n_split += 1
        c.metadata.is_leaf = False
        for j, piece in enumerate(pieces, start=1):
            leaf = Chunk(
                content=piece,
                summary=c.summary,          # all pieces share the parent block's summary
                keywords=list(c.keywords), features=list(c.features),
                workflows=list(c.workflows), personas=list(c.personas),
                entities=list(c.entities),
            )
            leaf.metadata.chunk_type = c.metadata.chunk_type
            leaf.metadata.sub_type   = c.metadata.sub_type
            leaf.metadata.headings   = c.metadata.headings + [f"part-{j}"]
            leaf.metadata.depth      = c.metadata.depth + 1
            leaf.metadata.is_leaf    = True
            leaf.metadata.parent_id  = c.chunk_id
            c.metadata.children_ids.append(leaf.chunk_id)
            out.append(leaf)
    logger.info("Recursive re-chunk: %d blocks in → %d chunks out (%d blocks split)",
                len(chunks), len(out), n_split)
    return out



# ── Pre-embedding filter + sibling packer ────────────────────────────────────
#
# WHY THIS EXISTS
#   After LLM extraction each window produces many small atomic blocks:
#     • keywords/personas blocks: comma-separated lists (8–15 tokens). These are
#       facet metadata, not retrieval prose. Embedding them pollutes the ANN index
#       with near-zero-information vectors and hurts retrieval precision.
#     • Sub-threshold fragments: any block below CHUNK_LEAF_MIN_TOKENS is noise.
#     • Sibling prose blocks (features/entities/workflows/knowledge) share the
#       same window root. Packing them into composite chunks before embedding
#       raises the per-vector token count toward the 512-token target so each
#       retrieval hit covers a denser, more useful passage.
#
# DESIGN CONTRACT
#   • keywords and personas are NEVER embedded (they remain in the full chunk
#     list for markdown/JSONL output — they are only excluded from Milvus).
#   • Chunks below CHUNK_LEAF_MIN_TOKENS are silently skipped.
#   • Prose siblings from the same window root are packed greedily up to
#     CHUNK_TARGET_TOKENS. If a block already fills the budget it is emitted
#     alone. The packed composite chunk inherits the first sibling's metadata
#     (type, sub_type, headings, parent_id) and carries the joined content.
#   • The original per-block Chunk objects are NOT mutated; new composite
#     Chunk objects are created for the packed groups.

_EMBED_SKIP_TYPES = frozenset({
    ChunkCategory.KEYWORDS.value,
    ChunkCategory.PERSONAS.value,
})


def _pack_and_filter_for_embedding(
    chunks: list[Chunk],
    settings,
) -> list[Chunk]:
    """Return the embed-ready subset of *chunks*.

    1. Drops keywords / personas blocks entirely.
    2. Drops chunks below ``chunk_leaf_min_tokens``.
    3. Groups remaining leaf blocks by their window root (parent_id) and packs
       consecutive siblings into composite chunks up to ``chunk_target_tokens``
       so each stored vector covers a denser passage.

    Non-leaf nodes (is_leaf=False, i.e. window roots) are kept as-is because
    they carry the roll-up summary for the whole window and are lightweight.
    """
    from src.services.ingestion.chunkers.splitter import default_token_len

    min_tokens    = int(getattr(settings, "chunk_leaf_min_tokens", 20))
    target_tokens = int(getattr(settings, "chunk_target_tokens",  512))
    cpt           = float(getattr(settings, "chars_per_token",     4.5))

    def _tok(text: str) -> int:
        return default_token_len(text, cpt)

    def _make_chunk(group_texts: list[str], anch: Chunk, composite: bool) -> Chunk:
        """Materialise one embed-ready Chunk from a group of content strings."""
        text = "\n\n".join(group_texts) if composite else group_texts[0]
        c = Chunk(
            content=text,
            summary=anch.summary,
            keywords=list(anch.keywords),
            features=list(anch.features),
            workflows=list(anch.workflows),
            personas=list(anch.personas),
            entities=list(anch.entities),
        )
        c.metadata.chunk_type = anch.metadata.chunk_type
        c.metadata.sub_type   = anch.metadata.sub_type
        c.metadata.headings   = list(anch.metadata.headings)
        c.metadata.depth      = anch.metadata.depth
        c.metadata.is_leaf    = True
        c.metadata.parent_id  = anch.metadata.parent_id
        return c

    # ── pass 1: hard filters ──────────────────────────────────────────────────
    candidates: list[Chunk] = []
    n_skip_type = 0
    n_skip_tiny = 0
    for c in chunks:
        if c.metadata.chunk_type.value in _EMBED_SKIP_TYPES:
            n_skip_type += 1
            continue
        if _tok(c.content) < min_tokens:
            n_skip_tiny += 1
            continue
        candidates.append(c)

    # ── pass 2: pack sibling leaves per window root ───────────────────────────
    # Group leaf blocks by parent_id.  Non-leaf roots are passed through
    # unchanged (they have no parent, so they land in the None bucket).
    from collections import defaultdict as _dd
    by_parent: dict[str | None, list[Chunk]] = _dd(list)
    non_leaf:  list[Chunk] = []
    for c in candidates:
        if c.metadata.is_leaf and c.metadata.parent_id is not None:
            by_parent[c.metadata.parent_id].append(c)
        else:
            non_leaf.append(c)

    packed: list[Chunk] = list(non_leaf)
    n_composite = 0
    for siblings in by_parent.values():
        group:      list[str] = []
        group_toks: int       = 0
        anchor:     Chunk     = siblings[0]

        for sib in siblings:
            tok = _tok(sib.content)
            if group and group_toks + tok > target_tokens:
                # flush current group
                packed.append(_make_chunk(group, anchor, len(group) > 1))
                if len(group) > 1:
                    n_composite += 1
                group      = [sib.content]
                group_toks = tok
                anchor     = sib
            else:
                group.append(sib.content)
                group_toks += tok

        if group:  # flush last group
            packed.append(_make_chunk(group, anchor, len(group) > 1))
            if len(group) > 1:
                n_composite += 1

    logger.info(
        "embed filter: %d total → skip_type=%d  skip_tiny=%d  "
        "candidates=%d  packed=%d  composite_groups=%d",
        len(chunks), n_skip_type, n_skip_tiny,
        len(candidates), len(packed), n_composite,
    )
    return packed


# ── Step 9: markdown persistence ──────────────────────────────────────────────

def _sim_hash(text: str, n: int = 8) -> str:
    """Return a short fingerprint of the first *n* words for content-level dedup."""
    words = re.sub(r"[^a-z0-9 ]+", "", text.lower()).split()
    return " ".join(words[:n])


def write_content_markdown(chunks: list[Chunk], out_dir: Path, doc_name: str) -> dict[str, str]:
    """
    Markdown of ALL content per entity type: one <CATEGORY>.md per category.
    Applies a duplicate engine — deduplicates by (name, content-fingerprint)
    so variant blocks about the same topic with new detail are kept, but
    exact-content duplicates are dropped.
    Returns {category: markdown_text}.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    docs: dict[str, str] = {}
    by_cat: dict[str, list[Chunk]] = {}
    for c in chunks:
        if c.metadata.parent_id is None or c.metadata.depth <= 2:   # blocks only
            by_cat.setdefault(c.metadata.chunk_type.value, []).append(c)
    for cat, items in by_cat.items():
        lines = [f"# {cat.title()} — {doc_name}", ""]
        seen_names: set[str]    = set()
        seen_content: set[str]  = set()
        n_written = 0
        for c in sorted(items, key=lambda x: x.metadata.headings[0].lower()):
            name = c.metadata.headings[0]
            fp   = _sim_hash(c.content)
            # Allow same name if content fingerprint is new (MERGE-relaxed blocks)
            key  = f"{name.lower()}||{fp}"
            if key in seen_names:
                continue
            # Hard-drop exact-content duplicates regardless of name
            if fp in seen_content:
                continue
            seen_names.add(key)
            seen_content.add(fp)
            n_written += 1
            lines += [f"## {name}", "", c.content.strip(), ""]
        md = "\n".join(lines)
        docs[cat] = md
        (out_dir / f"{cat.upper()}.md").write_text(md, encoding="utf-8")
        logger.info("Wrote full-content markdown: %s.md (%d sections)", cat.upper(), n_written)
    return docs


def write_summary_markdown(
    chunks: list[Chunk],
    out_dir: Path,
    doc_name: str,
    summary_dir: Path | None = None,
) -> None:
    """
    Write per-category summary Markdown.

    Writes to two locations:
      • out_dir/<CAT>_SUMMARY.md   — per-run output (for auditing)
      • summary_dir/<CAT>.md       — uploads/summary/ (used by retrieval)

    Applies the duplicate engine: deduplicates by (name, content-fingerprint)
    so the same entity with new window-variant detail is kept once per variant,
    but byte-identical summaries are collapsed.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    if summary_dir is not None:
        summary_dir.mkdir(parents=True, exist_ok=True)

    by_cat: dict[str, list[Chunk]] = {}
    for c in chunks:
        by_cat.setdefault(c.metadata.chunk_type.value, []).append(c)

    for cat, items in by_cat.items():
        header_lines = [
            f"# {cat.title()} — {doc_name}",
            f"_generated {datetime.now(timezone.utc).isoformat()}_",
            "", "---", "",
        ]
        body_lines: list[str] = []
        seen_keys:    set[str] = set()
        seen_content: set[str] = set()
        n_written = 0

        for c in sorted(items, key=lambda x: x.metadata.headings[0].lower()):
            name    = c.metadata.headings[0]
            summary = (c.summary or c.content[:400]).strip()
            fp      = _sim_hash(summary)
            key     = f"{name.lower()}||{fp}"
            if key in seen_keys:
                continue
            if fp in seen_content:
                continue
            seen_keys.add(key)
            seen_content.add(fp)
            n_written += 1

            body_lines += [f"## {name}", "", summary, ""]
            rels = [f"**{lbl}:** {', '.join(vals)}"
                    for lbl, vals in (("Keywords", c.keywords), ("Features", c.features),
                                      ("Workflows", c.workflows), ("Personas", c.personas),
                                      ("Entities", c.entities)) if vals]
            if rels:
                body_lines += ["  \n".join(rels), ""]
            body_lines += ["---", ""]

        md = "\n".join(header_lines + body_lines)

        # Per-run summary (audit copy)
        (out_dir / f"{cat.upper()}_SUMMARY.md").write_text(md, encoding="utf-8")
        # Live summary used by retrieval (uploads/summary/<CAT>.md)
        if summary_dir is not None:
            (summary_dir / f"{cat.upper()}.md").write_text(md, encoding="utf-8")

        logger.info(
            "Wrote %d %s summaries → %s_SUMMARY.md%s",
            n_written, cat, cat.upper(),
            f" + uploads/summary/{cat.upper()}.md" if summary_dir else "",
        )


# ── Orchestrator ──────────────────────────────────────────────────────────────

class EntityPipeline:
    """Runs the full window-based extraction flow.

    All LLM-heavy and I/O-heavy steps are async so the event loop is shared
    across the whole pipeline run — no nested asyncio.run() calls.
    The public entry point is run_async(); run() wraps it for sync callers.
    """

    def __init__(self):
        self.settings  = get_settings()
        self.processor = DocumentProcessor()
        self.llm       = LLMService()
        self.embedder  = EmbeddingService()
        self.writer    = OutputWriterService()
        self.milvus    = MilvusService()

    # steps 1-2 ---------------------------------------------------------------
    def load_and_clean(self, source: str, source_type: SourceType) -> Document:
        doc = get_loader(source_type).load(source)
        return self.processor.process(doc)

    # steps 3-5 ---------------------------------------------------------------
    async def extract(self, doc: Document) -> list[Chunk]:
        """Window the document, build the domain profile, then run extraction.

        Mode is controlled by LLM_EXTRACTION_MODE (settings.llm_extraction_mode):
          "all_types"   — one LLM call per window, all six types in one reply (default)
          "sequential"  — ROUTER call per window to inventory facts, then one focused
                          typed-pass per category found, run as 6 serial batches
                          (more LLM calls, smaller/focused prompts, highest fidelity,
                           slowest: each batch waits for the previous to finish)
          "parallel"    — ROUTER call per window (same as sequential), then all 6
                          typed passes for ALL windows are dispatched into one combined
                          LLM pool and run concurrently (same call count as sequential,
                          wall-clock ≈ all_types; requires LLM_CONCURRENCY >= 2)
          "independent" — NO ROUTER. 6 direct per-category LLM passes fired in
                          parallel for every window. Each pass uses only its own
                          TYPE_PROMPTS[category] system prompt + DIRECT_USER message.
                          Implements the exact independent-lane schema:
                            stage2_cleaned → [Chunk] → LLM(knowledge prompt) → [Knowledge]
                              → {chunk_id, chunk_type, sub_type, depth, is_leaf,
                                 parent_id, children_ids, content_hash, summary,
                                 content, embedding, summary_embedding}
                            stage2_cleaned → [Chunk] → LLM(keywords prompt)  → [Keyword]
                              → {same full schema}
                            … (personas, workflows, features, entities follow)
        """
        windows = make_windows(doc.cleaned_content)          # step 3
        windows = llm_clean_windows(self.llm, windows)       # step 4 (no-op by default)

        loop         = asyncio.get_running_loop()
        domain_terms = await loop.run_in_executor(
            None, build_domain_profile, doc.cleaned_content
        )

        mode = getattr(self.settings, "llm_extraction_mode", "all_types").lower()
        if mode == "sequential":
            return await self._extract_sequential(doc, windows, domain_terms, loop)
        if mode == "parallel":
            return await self._extract_parallel(doc, windows, domain_terms, loop)
        if mode == "independent":
            return await self._extract_independent(doc, windows, domain_terms, loop)
        return await self._extract_all_types(doc, windows, domain_terms, loop)

    # ── extraction mode: all-types (original) ─────────────────────────────────

    async def _extract_all_types(
        self,
        doc: "Document",
        windows: list[str],
        domain_terms: str,
        loop: asyncio.AbstractEventLoop,
    ) -> list[Chunk]:
        """One LLM call per window — extracts all six block types in one reply."""
        # Compact schema drops Evidence + the 5 cross-ref lines: ~40% fewer
        # output tokens, and decode is what the wall clock is made of.
        _tmpl = (ALL_TYPES_SYSTEM_COMPACT
                 if getattr(self.settings, "llm_compact_schema", False)
                 else ALL_TYPES_SYSTEM)
        extract_system = _tmpl.format(domain_terms=domain_terms)

        reqs = [
            (extract_system,
             ALL_TYPES_USER.format(doc_name=doc.doc_id, index=i + 1,
                                   total=len(windows), text=w))
            for i, w in enumerate(windows)
        ]

        logger.info(
            "EXTRACT ALL_TYPES START  doc=%s  windows=%d  window_chars=%d  concurrency=%d",
            doc.doc_id, len(windows),
            max((len(w) for w in windows), default=0),
            getattr(self.settings, "llm_concurrency", 4),
        )

        _total_windows = len(windows)

        def _on_window_result(idx: int, raw: str) -> None:
            pass

        responses = await loop.run_in_executor(
            None, self.llm.complete_batch, reqs, _on_window_result
        )

        succeeded  = [i + 1 for i, r in enumerate(responses) if r]
        failed_idx = [i      for i, r in enumerate(responses) if not r]
        logger.info(
            "EXTRACT ALL_TYPES BATCH RESULT  succeeded=%d/%d  failed=%d  "
            "succeeded_windows=%s  failed_windows=%s",
            len(succeeded), len(windows), len(failed_idx),
            succeeded[:20], [i + 1 for i in failed_idx[:20]],
        )

        if failed_idx and self.llm.enabled:
            logger.warning(
                "EXTRACT RETRY  %d/%d windows empty — re-submitting concurrency=3  windows=%s",
                len(failed_idx), len(windows), [i + 1 for i in failed_idx],
            )
            retry_reqs = [reqs[i] for i in failed_idx]
            retry_responses = await loop.run_in_executor(
                None, self.llm.complete_batch_retry, retry_reqs
            )
            recovered = 0
            recovered_windows:    list[int] = []
            still_empty_windows:  list[int] = []
            for list_pos, orig_idx in enumerate(failed_idx):
                if retry_responses[list_pos]:
                    responses[orig_idx] = retry_responses[list_pos]
                    recovered += 1
                    recovered_windows.append(orig_idx + 1)
                else:
                    still_empty_windows.append(orig_idx + 1)
            logger.info(
                "EXTRACT RETRY DONE  recovered=%d/%d  still_empty=%d  "
                "recovered_windows=%s  failed_windows=%s",
                recovered, len(failed_idx), len(failed_idx) - recovered,
                recovered_windows, still_empty_windows,
            )

        chunks: list[Chunk] = []
        by_type: dict[str, int] = {}
        empty_windows: list[int] = []
        for i, raw in enumerate(responses):
            if not raw:
                empty_windows.append(i + 1)
                logger.warning("Window %d/%d → EMPTY response (LLM failed/timed out)",
                               i + 1, len(windows))
                continue
            recs = parse_blocks(raw)
            for r in recs:
                by_type[r["type"]] = by_type.get(r["type"], 0) + 1
            logger.info("Window %d/%d → %d blocks  raw_resp_chars=%d  types=%s",
                        i + 1, len(windows), len(recs), len(raw),
                        {k: v for k, v in sorted(by_type.items())})
            chunks.extend(records_to_chunks(recs, i + 1))

        logger.info(
            "EXTRACT DONE  windows=%d  empty=%d  total_chunks=%d  by_type=%s",
            len(windows), len(empty_windows), len(chunks),
            {k: v for k, v in sorted(by_type.items())},
        )
        if empty_windows:
            logger.warning("Empty LLM responses for windows: %s", empty_windows)
        return chunks

    # ── extraction mode: sequential per-category ──────────────────────────────

    async def _extract_sequential(
        self,
        doc: "Document",
        windows: list[str],
        domain_terms: str,
        loop: asyncio.AbstractEventLoop,
    ) -> list[Chunk]:
        """ROUTER → typed passes — one category at a time per window.

        For each window:
          1. Run the ROUTER prompt — a cheap call that inventories every fact and
             assigns each to exactly one type.  The manifest it produces is fed to
             every subsequent typed pass so each pass knows exactly what it owns.
          2. Parse the router manifest to discover which categories are present
             in this window (avoids wasting an LLM call on an absent category).
          3. For each category found (in EXTRACTION_ORDER), fire ONE focused typed
             pass that only extracts that category — smaller prompt, less context
             competition, better fidelity.

        Categories are processed one at a time (not blasted concurrently) so the
        AIM endpoint is not flooded with N_windows × 6 calls simultaneously.
        Concurrency within a single category's batch is still controlled by
        LLM_CONCURRENCY as usual.
        """
        router_system = ROUTER_SYSTEM.format(domain_terms=domain_terms)
        router_reqs   = [
            (router_system,
             ROUTER_USER.format(doc_name=doc.doc_id, index=i + 1,
                                total=len(windows), text=w))
            for i, w in enumerate(windows)
        ]

        logger.info(
            "EXTRACT SEQUENTIAL START  doc=%s  windows=%d  categories=%s",
            doc.doc_id, len(windows), EXTRACTION_ORDER,
        )

        # ── PASS 0: ROUTER — one call per window ──────────────────────────────
        logger.info("EXTRACT SEQUENTIAL  pass=ROUTER  windows=%d", len(windows))
        router_responses = await loop.run_in_executor(
            None, self.llm.complete_batch, router_reqs
        )
        failed_router = [i for i, r in enumerate(router_responses) if not r]
        if failed_router and self.llm.enabled:
            logger.warning(
                "EXTRACT SEQUENTIAL ROUTER RETRY  failed=%d  windows=%s",
                len(failed_router), [i + 1 for i in failed_router],
            )
            retry_resp = await loop.run_in_executor(
                None, self.llm.complete_batch_retry,
                [router_reqs[i] for i in failed_router],
            )
            for list_pos, orig_idx in enumerate(failed_router):
                if retry_resp[list_pos]:
                    router_responses[orig_idx] = retry_resp[list_pos]
        logger.info(
            "EXTRACT SEQUENTIAL ROUTER DONE  succeeded=%d/%d",
            sum(1 for r in router_responses if r), len(windows),
        )

        # ── PASS 1..6: one typed pass per category, fired as a batch ──────────
        # Collect records grouped by 0-based window index so records_to_chunks
        # receives ALL categories for a window at once (needed for the
        # knowledge-root parent/child tree that records_to_chunks builds).
        recs_by_window: dict[int, list[dict]] = {i: [] for i in range(len(windows))}

        for category in EXTRACTION_ORDER:
            cat_system = TYPE_PROMPTS[category].format(domain_terms=domain_terms)

            # Build requests only for windows where the router found this category.
            # Windows where the router failed fall back to sending the full window
            # text without a manifest so we don't silently drop facts.
            cat_reqs: list[tuple[str, str]] = []
            win_map:  list[int] = []           # maps cat_reqs index → 0-based window index

            for i, (w, router_raw) in enumerate(zip(windows, router_responses)):
                manifest = router_raw or ""
                # Heuristic: skip this window for this category only when the
                # router succeeded AND this category name does not appear in the
                # manifest at all.  If the router failed, always include the window
                # so no facts are silently dropped.
                if manifest and category not in manifest.lower():
                    continue
                user_msg = TYPED_USER.format(
                    doc_name=doc.doc_id,
                    index=i + 1,
                    total=len(windows),
                    type_name=category,
                    manifest=manifest or "(router unavailable — extract all facts of this type)",
                    text=w,
                )
                cat_reqs.append((cat_system, user_msg))
                win_map.append(i)

            if not cat_reqs:
                logger.info(
                    "EXTRACT SEQUENTIAL  pass=%s  skipped — category absent in all router manifests",
                    category,
                )
                continue

            logger.info(
                "EXTRACT SEQUENTIAL  pass=%s  windows_with_category=%d/%d",
                category, len(cat_reqs), len(windows),
            )

            # Fire this category's batch; respect rate-limit pacing via complete_batch.
            cat_responses = await loop.run_in_executor(
                None, self.llm.complete_batch, cat_reqs
            )

            # Retry any empty responses at concurrency=3.
            failed_cat = [j for j, r in enumerate(cat_responses) if not r]
            if failed_cat and self.llm.enabled:
                logger.warning(
                    "EXTRACT SEQUENTIAL  pass=%s  retrying %d empty responses  concurrency=3",
                    category, len(failed_cat),
                )
                retry_cat = await loop.run_in_executor(
                    None, self.llm.complete_batch_retry,
                    [cat_reqs[j] for j in failed_cat],
                )
                for list_pos, orig_j in enumerate(failed_cat):
                    if retry_cat[list_pos]:
                        cat_responses[orig_j] = retry_cat[list_pos]

            for j, raw in enumerate(cat_responses):
                win_idx = win_map[j]   # 0-based window index
                if not raw or raw.strip().upper() == "NONE FOR THIS TYPE":
                    continue
                recs = parse_blocks(raw)
                if recs:
                    recs_by_window[win_idx].extend(recs)   # accumulate into window bucket
                    logger.debug(
                        "EXTRACT SEQUENTIAL  pass=%s  window=%d  blocks=%d",
                        category, win_idx + 1, len(recs),
                    )

            logger.info(
                "EXTRACT SEQUENTIAL  pass=%s  done  cat_windows=%d",
                category, len(cat_reqs),
            )

        # ── Merge all records into Chunk objects — one call per window ─────────
        # records_to_chunks must receive all categories for a window together so
        # it can locate the knowledge root and wire the parent/child tree.
        chunks: list[Chunk] = []
        by_type: dict[str, int] = {}
        empty_windows: list[int] = []
        for win_idx, recs in recs_by_window.items():
            if not recs:
                empty_windows.append(win_idx + 1)
                continue
            for r in recs:
                by_type[r["type"]] = by_type.get(r["type"], 0) + 1
            logger.info(
                "Window %d/%d → %d blocks  types=%s",
                win_idx + 1, len(windows), len(recs),
                {k: v for k, v in sorted(by_type.items())},
            )
            chunks.extend(records_to_chunks(recs, win_idx + 1))

        logger.info(
            "EXTRACT SEQUENTIAL DONE  windows=%d  empty=%d  total_chunks=%d  by_type=%s",
            len(windows), len(empty_windows), len(chunks),
            {k: v for k, v in sorted(by_type.items())},
        )
        if empty_windows:
            logger.warning("Empty sequential extraction for windows: %s", empty_windows)
        return chunks

    # ── extraction mode: parallel per-category ───────────────────────────────

    async def _extract_parallel(
        self,
        doc: "Document",
        windows: list[str],
        domain_terms: str,
        loop: asyncio.AbstractEventLoop,
    ) -> list[Chunk]:
        """ROUTER → all 6 typed passes fired concurrently in a single LLM pool.

        Difference from sequential:
          - sequential fires 6 serial complete_batch() sweeps (each sweep waits
            for ALL windows to finish before the next category starts)
          - parallel builds ONE flat request list of up to N_windows × 6 typed
            requests and hands it to a single complete_batch() call. The worker
            pool (LLM_CONCURRENCY slots) drains all requests concurrently —
            no artificial inter-pass barriers.

        Wall-clock time is therefore bounded by the slowest single request
        rather than by the sum of 6 sweeps.  Call count and prompt quality are
        identical to sequential.

        Each request is tagged with (window_index, category) so results can be
        reassembled per-window for records_to_chunks().
        """
        router_system = ROUTER_SYSTEM.format(domain_terms=domain_terms)
        router_reqs   = [
            (router_system,
             ROUTER_USER.format(doc_name=doc.doc_id, index=i + 1,
                                total=len(windows), text=w))
            for i, w in enumerate(windows)
        ]

        logger.info(
            "EXTRACT PARALLEL START  doc=%s  windows=%d  categories=%s",
            doc.doc_id, len(windows), EXTRACTION_ORDER,
        )

        # ── PASS 0: ROUTER — identical to sequential ──────────────────────────
        logger.info("EXTRACT PARALLEL  pass=ROUTER  windows=%d", len(windows))
        router_responses = await loop.run_in_executor(
            None, self.llm.complete_batch, router_reqs
        )
        failed_router = [i for i, r in enumerate(router_responses) if not r]
        if failed_router and self.llm.enabled:
            logger.warning(
                "EXTRACT PARALLEL ROUTER RETRY  failed=%d  windows=%s",
                len(failed_router), [i + 1 for i in failed_router],
            )
            retry_resp = await loop.run_in_executor(
                None, self.llm.complete_batch_retry,
                [router_reqs[i] for i in failed_router],
            )
            for list_pos, orig_idx in enumerate(failed_router):
                if retry_resp[list_pos]:
                    router_responses[orig_idx] = retry_resp[list_pos]
        logger.info(
            "EXTRACT PARALLEL ROUTER DONE  succeeded=%d/%d",
            sum(1 for r in router_responses if r), len(windows),
        )

        # ── PASS 1..6: build ALL typed requests in one flat list ──────────────
        # Each entry in typed_reqs carries a (win_idx, category) tag so we can
        # reassemble results after the single combined complete_batch() call.
        typed_reqs: list[tuple[str, str]] = []
        req_tags:   list[tuple[int, str]] = []   # parallel to typed_reqs

        for i, (w, router_raw) in enumerate(zip(windows, router_responses)):
            manifest = router_raw or ""
            for category in EXTRACTION_ORDER:
                # Skip this (window, category) pair only when the router
                # succeeded AND reported no items of this type.
                if manifest and category not in manifest.lower():
                    continue
                cat_system = TYPE_PROMPTS[category].format(domain_terms=domain_terms)
                user_msg = TYPED_USER.format(
                    doc_name=doc.doc_id,
                    index=i + 1,
                    total=len(windows),
                    type_name=category,
                    manifest=manifest or "(router unavailable — extract all facts of this type)",
                    text=w,
                )
                typed_reqs.append((cat_system, user_msg))
                req_tags.append((i, category))

        logger.info(
            "EXTRACT PARALLEL  typed_requests=%d  across_windows=%d  categories=%d",
            len(typed_reqs), len(windows), len(EXTRACTION_ORDER),
        )

        if not typed_reqs:
            logger.warning("EXTRACT PARALLEL  no typed requests built — returning empty")
            return []

        # Fire all typed requests in one pool — LLM_CONCURRENCY controls
        # how many run simultaneously across windows AND categories at once.
        typed_responses = await loop.run_in_executor(
            None, self.llm.complete_batch, typed_reqs
        )

        # Retry any failures at concurrency=3.
        failed_typed = [j for j, r in enumerate(typed_responses) if not r]
        if failed_typed and self.llm.enabled:
            logger.warning(
                "EXTRACT PARALLEL  retrying %d/%d empty typed responses  concurrency=3",
                len(failed_typed), len(typed_reqs),
            )
            retry_typed = await loop.run_in_executor(
                None, self.llm.complete_batch_retry,
                [typed_reqs[j] for j in failed_typed],
            )
            for list_pos, orig_j in enumerate(failed_typed):
                if retry_typed[list_pos]:
                    typed_responses[orig_j] = retry_typed[list_pos]

        # ── Reassemble: accumulate records per window ─────────────────────────
        recs_by_window: dict[int, list[dict]] = {i: [] for i in range(len(windows))}
        for j, raw in enumerate(typed_responses):
            win_idx, category = req_tags[j]
            if not raw or raw.strip().upper() == "NONE FOR THIS TYPE":
                continue
            recs = parse_blocks(raw)
            if recs:
                recs_by_window[win_idx].extend(recs)
                logger.debug(
                    "EXTRACT PARALLEL  category=%s  window=%d  blocks=%d",
                    category, win_idx + 1, len(recs),
                )

        # ── Build Chunk objects — one call per window ─────────────────────────
        chunks: list[Chunk] = []
        by_type: dict[str, int] = {}
        empty_windows: list[int] = []
        for win_idx, recs in recs_by_window.items():
            if not recs:
                empty_windows.append(win_idx + 1)
                continue
            for r in recs:
                by_type[r["type"]] = by_type.get(r["type"], 0) + 1
            logger.info(
                "Window %d/%d → %d blocks  types=%s",
                win_idx + 1, len(windows), len(recs),
                {k: v for k, v in sorted(by_type.items())},
            )
            chunks.extend(records_to_chunks(recs, win_idx + 1))

        logger.info(
            "EXTRACT PARALLEL DONE  windows=%d  empty=%d  total_chunks=%d  by_type=%s",
            len(windows), len(empty_windows), len(chunks),
            {k: v for k, v in sorted(by_type.items())},
        )
        if empty_windows:
            logger.warning("Empty parallel extraction for windows: %s", empty_windows)
        return chunks

    # ── extraction mode: independent (direct per-category, no router) ─────────

    async def _extract_independent(
        self,
        doc: "Document",
        windows: list[str],
        domain_terms: str,
        loop: asyncio.AbstractEventLoop,
    ) -> list[Chunk]:
        """NO ROUTER — 6 direct per-category LLM passes fired in parallel.

        Implements the exact independent-lane schema the user specified:

            stage2_cleaned → [Chunk] → LLM(knowledge prompt) → [Knowledge]
              → {chunk_id, chunk_type, sub_type, depth, is_leaf,
                 parent_id, children_ids, content_hash,
                 summary, content, embedding, summary_embedding}

            stage2_cleaned → [Chunk] → LLM(keywords prompt)  → [Keyword]
              → {same full schema, chunk_type="keywords"}

            stage2_cleaned → [Chunk] → LLM(personas prompt)  → [Persona]
              → {same full schema, chunk_type="personas"}

            stage2_cleaned → [Chunk] → LLM(workflows prompt) → [Workflow]
              → {same full schema, chunk_type="workflows"}

            stage2_cleaned → [Chunk] → LLM(features prompt)  → [Feature]
              → {same full schema, chunk_type="features"}

            stage2_cleaned → [Chunk] → LLM(entities prompt)  → [Entity]
              → {same full schema, chunk_type="entities"}

        All 6 × N_windows requests are placed into ONE flat batch so the
        LLM provider's concurrency pool (LLM_CONCURRENCY) drains them with
        maximum parallelism — same wall-clock behaviour as "parallel" but
        without the ROUTER overhead.

        Each chunk carries:
          • chunk_type   set to its extraction category
          • sub_type     set from the LLM SubType field
          • depth=2, is_leaf=True, parent_id → window root knowledge chunk
          • summary filled by the LLM Summary field (not a separate pass)
          • content, embedding, summary_embedding filled downstream

        The knowledge pass is always included; its chunks become the window
        root nodes (depth=1) that all other category chunks hang from.
        """
        logger.info(
            "EXTRACT INDEPENDENT START  doc=%s  windows=%d  categories=%s",
            doc.doc_id, len(windows), EXTRACTION_ORDER,
        )

        # Build one (system, user) request per (window, category) pair.
        # Tags track which result belongs to which (window_index, category).
        all_reqs:  list[tuple[str, str]]  = []
        req_tags:  list[tuple[int, str]]  = []   # (0-based window idx, category)

        for i, w in enumerate(windows):
            for category in EXTRACTION_ORDER:
                system = TYPE_PROMPTS[category].format(domain_terms=domain_terms)
                user   = DIRECT_USER.format(
                    doc_name=doc.doc_id,
                    index=i + 1,
                    total=len(windows),
                    type_name=category,
                    text=w,
                )
                all_reqs.append((system, user))
                req_tags.append((i, category))

        logger.info(
            "EXTRACT INDEPENDENT  total_requests=%d  (windows=%d × categories=%d)",
            len(all_reqs), len(windows), len(EXTRACTION_ORDER),
        )

        # Fire all requests in one pool — LLM_CONCURRENCY controls parallelism.
        responses = await loop.run_in_executor(
            None, self.llm.complete_batch, all_reqs
        )

        # Retry any failures at concurrency=3.
        failed = [j for j, r in enumerate(responses) if not r]
        if failed and self.llm.enabled:
            logger.warning(
                "EXTRACT INDEPENDENT  retrying %d/%d empty responses  concurrency=3",
                len(failed), len(all_reqs),
            )
            retry = await loop.run_in_executor(
                None, self.llm.complete_batch_retry,
                [all_reqs[j] for j in failed],
            )
            for list_pos, orig_j in enumerate(failed):
                if retry[list_pos]:
                    responses[orig_j] = retry[list_pos]

        # Accumulate records per window so records_to_chunks() sees all
        # categories together and can build the knowledge-root parent/child tree.
        recs_by_window: dict[int, list[dict]] = {i: [] for i in range(len(windows))}
        by_type: dict[str, int] = {}

        for j, (raw, (win_idx, category)) in enumerate(zip(responses, req_tags)):
            if not raw or raw.strip().upper() == "NONE FOR THIS TYPE":
                continue
            recs = parse_blocks(raw)
            # Force every record to the correct category — the per-category
            # system prompt should enforce this, but pin it defensively so a
            # stray "Type: knowledge" in a personas pass doesn't pollute the tree.
            for r in recs:
                r["type"] = category
            if recs:
                recs_by_window[win_idx].extend(recs)
                for r in recs:
                    by_type[r["type"]] = by_type.get(r["type"], 0) + 1
                logger.debug(
                    "EXTRACT INDEPENDENT  cat=%-12s  window=%d  blocks=%d",
                    category, win_idx + 1, len(recs),
                )

        # Convert per-window record groups into Chunk objects.
        # records_to_chunks() locates the knowledge root and wires parent/child.
        chunks: list[Chunk] = []
        empty_windows: list[int] = []
        for win_idx in range(len(windows)):
            recs = recs_by_window[win_idx]
            if not recs:
                empty_windows.append(win_idx + 1)
                continue
            logger.info(
                "Window %d/%d → %d blocks  types=%s",
                win_idx + 1, len(windows), len(recs),
                {k: v for k, v in sorted(by_type.items())},
            )
            chunks.extend(records_to_chunks(recs, win_idx + 1))

        logger.info(
            "EXTRACT INDEPENDENT DONE  windows=%d  empty=%d  "
            "total_chunks=%d  by_type=%s",
            len(windows), len(empty_windows), len(chunks),
            {k: v for k, v in sorted(by_type.items())},
        )
        if empty_windows:
            logger.warning(
                "EXTRACT INDEPENDENT  empty windows: %s", empty_windows
            )
        return chunks

    # steps 6-7 ---------------------------------------------------------------
    async def rechunk_and_summarize(self, chunks: list[Chunk]) -> list[Chunk]:
        """Recursive-chunk the LLM-processed content, then summarise every
        recursive piece so BOTH vectors exist for every stored chunk.

        CPU-bound re-chunking and LLM summarisation both run in an executor
        so they don't block the event loop.

        Each category is summarised independently using a category-aware system
        prompt (see SummarizerService.summarize_leaves), implementing the
        independent extraction lanes:

            Content → [Chunk] → [Knowledge] → {Summary:Knowledge}
              → {summary, content, summary_embedding, content_embedding}
            Content → [Chunk] → [Keyword]   → {Summary:Keyword}
              → {summary, keyword, summary_embedding, keyword_embedding}
            Content → [Chunk] → [Persona]   → {Summary:Persona}
              → {summary, persona, summary_embedding, persona_embedding}
            Content → [Chunk] → [Workflow]  → {Summary:Workflow}
              → {summary, workflow, summary_embedding, workflow_embedding}
        """
        from collections import defaultdict as _dd
        from src.services.ingestion.chunkers.summarizer import SummarizerService

        loop       = asyncio.get_running_loop()
        all_chunks = await loop.run_in_executor(None, recursive_rechunk, chunks)  # step 6

        new_leaves = [c for c in all_chunks if not c.summary]
        if new_leaves:                                                             # step 7
            # Log per-category leaf counts before summarisation so operators
            # can see how many chunks entered each independent lane.
            cat_counts: dict[str, int] = _dd(int)
            for c in new_leaves:
                cat_counts[c.metadata.chunk_type.value] += 1
            logger.info(
                "rechunk_and_summarize: %d new leaves across %d categories: %s",
                len(new_leaves), len(cat_counts),
                dict(sorted(cat_counts.items())),
            )
            svc = SummarizerService(llm_service=self.llm)
            await loop.run_in_executor(None, svc.summarize_leaves, new_leaves)
        return all_chunks

    # steps 8-9 ---------------------------------------------------------------
    async def embed_and_persist(self, chunks: list[Chunk], doc_name: str) -> dict:
        """Embed content + summary vectors, write markdown/JSONL, upsert to Milvus.

        Embedding (CPU/GPU) and Milvus upsert run concurrently via asyncio.gather
        after the embeddings are ready: content and summary embeddings are
        computed sequentially (they reuse the same model batch), then the
        Milvus upsert (async natively) runs directly in the event loop.

        Per-category embedding pair counts are logged after both embedding passes
        complete, matching the independent-lane schema:
            {summary, content, summary_embedding, content_embedding} per category.

        Pre-embedding filters applied here (before any vector work):
          1. keywords and personas chunks are facet metadata, not retrieval
             candidates — they are kept in the full chunk list for markdown/JSONL
             output but are excluded from the embed set sent to Milvus.
          2. Chunks below CHUNK_LEAF_MIN_TOKENS are noise fragments — excluded.
          3. Sibling leaves from the same window are packed into composite chunks
             so each stored vector covers a denser passage (target ≈ 512 tokens).
        """
        loop = asyncio.get_running_loop()

        # ── Pre-embedding: pack siblings + filter noise ───────────────────────
        embed_chunks = _pack_and_filter_for_embedding(chunks, self.settings)

        # Distillation and markdown writes are I/O-bound — run in executor
        # so they don't block embedding.
        distill_task = loop.run_in_executor(
            None, self._distill_summaries, chunks, doc_name
        )

        # Embeddings are CPU/GPU-bound — run both passes in the executor.
        # Only the filtered+packed set is embedded and sent to Milvus; the
        # full `chunks` list is still used for markdown/JSONL output below.
        async def _embed_all() -> None:
            await loop.run_in_executor(None, self.embedder.embed_chunks,   embed_chunks)
            await loop.run_in_executor(None, self.embedder.embed_summaries, embed_chunks)

        # Run distillation and embedding concurrently.
        await asyncio.gather(distill_task, _embed_all())

        # ── Per-category embedding pair audit ─────────────────────────────────
        # Report {content, summary, content_embedding, summary_embedding} counts
        # for each independent extraction lane so operators can verify that every
        # category produced a complete quad.
        self._log_category_embedding_pairs(embed_chunks)

        # Milvus upsert uses only the filtered+packed set.
        stored = await self.milvus.upsert_chunks(embed_chunks)
        return {"chunks": len(chunks), "stored": stored,
                "embed_chunks": len(embed_chunks)}

    @staticmethod
    def _log_category_embedding_pairs(chunks: list[Chunk]) -> None:
        """Log per-category {content, summary, content_embedding, summary_embedding}
        pair counts so operators can verify each independent extraction lane
        produced a complete quad.

        A 'complete quad' for a chunk means:
            content             — non-empty (always set by extraction)
            summary             — non-empty (set by SummarizerService or extractive fallback)
            embedding           — non-empty (set by EmbeddingService.embed_chunks)
            summary_embedding   — non-empty (set by EmbeddingService.embed_summaries)
        """
        from collections import defaultdict as _dd
        stats: dict[str, dict[str, int]] = _dd(lambda: {
            "total": 0,
            "has_content": 0,
            "has_summary": 0,
            "has_content_embedding": 0,
            "has_summary_embedding": 0,
            "complete_quad": 0,
        })
        for c in chunks:
            cat = c.metadata.chunk_type.value
            s = stats[cat]
            s["total"] += 1
            has_content   = bool(c.content.strip())
            has_summary   = bool(c.summary.strip())
            has_cemb      = bool(c.embedding)
            has_semb      = bool(c.summary_embedding)
            if has_content:   s["has_content"] += 1
            if has_summary:   s["has_summary"] += 1
            if has_cemb:      s["has_content_embedding"] += 1
            if has_semb:      s["has_summary_embedding"] += 1
            if has_content and has_summary and has_cemb and has_semb:
                s["complete_quad"] += 1

        for cat, s in sorted(stats.items()):
            logger.info(
                "EmbedPairs  cat=%-12s  total=%d  "
                "content=%d  summary=%d  "
                "content_emb=%d  summary_emb=%d  "
                "complete_quad=%d",
                cat, s["total"],
                s["has_content"], s["has_summary"],
                s["has_content_embedding"], s["has_summary_embedding"],
                s["complete_quad"],
            )

    def _distill_summaries(self, chunks: list[Chunk], doc_name: str) -> None:
        """Layer-3 distillation → summary.zip-format <CATEGORY>.md files."""
        from src.services.ingestion.summary_distiller import SummaryDistiller

        source_name = getattr(getattr(chunks[0], "metadata", None), "source_name", None) \
            if chunks else None
        source_name = source_name or doc_name

        distilled_dir = Path(self.settings.summary_dir)
        try:
            SummaryDistiller(self.llm, self.settings).distill(
                chunks, distilled_dir, source_name)
        except Exception as exc:
            logger.error("Summary distillation failed: %s", exc)

    # full run ------------------------------------------------------------------
    async def run_async(self, source: str,
                        source_type: SourceType = SourceType.PDF) -> dict:
        """Async entry point. Steps 1-2 are sync (I/O only); 3-9 are async."""
        doc    = self.load_and_clean(source, source_type)    # 1-2 sync
        blocks = await self.extract(doc)                     # 3-5 async LLM
        chunks = await self.rechunk_and_summarize(blocks)    # 6-7 async
        result = await self.embed_and_persist(chunks, doc.doc_id)  # 8-9 async
        logger.info("EntityPipeline done: %s", result)
        return result

    def run(self, source: str, source_type: SourceType = SourceType.PDF) -> dict:
        """Sync wrapper — creates a new event loop for callers that cannot await."""
        return asyncio.run(self.run_async(source, source_type))

    # ── Debug dump helpers ─────────────────────────────────────────────────────

    def _dump_doc(self, doc: "Document") -> None:
        """Write raw content and cleaned content to uploads/<doc_id>/."""
        import json as _json
        dump_dir = Path(self.settings.upload_dir) / doc.doc_id
        dump_dir.mkdir(parents=True, exist_ok=True)

        # raw extracted text (before DocumentProcessor)
        raw_path = dump_dir / "stage1_raw.txt"
        raw_path.write_text(doc.content, encoding="utf-8")

        # cleaned text (after DocumentProcessor)
        clean_path = dump_dir / "stage2_cleaned.txt"
        clean_path.write_text(doc.cleaned_content, encoding="utf-8")

        # metadata sidecar
        meta_path = dump_dir / "stage1_meta.json"
        meta_path.write_text(_json.dumps({
            "doc_id":            doc.doc_id,
            "source_name":       doc.metadata.source_name,
            "source_type":       doc.metadata.source_type.value,
            "original_filename": doc.metadata.original_filename,
            "raw_chars":         len(doc.content),
            "clean_chars":       len(doc.cleaned_content),
            "removed_chars":     len(doc.content) - len(doc.cleaned_content),
        }, indent=2), encoding="utf-8")

        logger.info(
            "DEBUG dump: stage1_raw.txt (%d chars)  stage2_cleaned.txt (%d chars)  → %s",
            len(doc.content), len(doc.cleaned_content), dump_dir,
        )

    # ── Incremental stage3 helpers ────────────────────────────────────────────

    def _stage3_path(self, doc_id: str) -> "Path":
        return Path(self.settings.upload_dir) / doc_id / "stage3_content_all.txt"

    def _init_stage3_file(self, doc_id: str) -> None:
        """Create (or truncate) stage3_content_all.txt and write the header.

        Called once before extraction starts so the file exists and is empty.
        Subsequent per-window appends then grow it incrementally.
        """
        path = self._stage3_path(doc_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"# Stage-3 extracted content — ALL blocks\n"
            f"# doc_id : {doc_id}\n"
            f"# (appended incrementally — one window at a time)\n\n",
            encoding="utf-8",
        )
        logger.debug("stage3_content_all.txt initialised → %s", path)

    def _append_window_stage3(
        self, doc_id: str, recs: list[dict], win_idx: int, total_windows: int
    ) -> None:
        """Append the blocks from one window to stage3_content_all.txt immediately
        after the LLM response for that window is parsed.

        This lets you tail -f the file and watch extraction progress in real time
        rather than waiting for the entire document to finish.
        """
        DIVIDER = "─" * 72

        def _block_lines(rec: dict) -> list[str]:
            lines = [
                DIVIDER,
                f"[{rec['type'].upper()}]  {rec['name']}"
                f"  |  sub_type={rec['sub_type']}"
                f"  |  window-{win_idx}"
                f"  |  tokens={rec.get('token_count', '?')}",
                "",
                rec["content"].strip() or "(empty)",
            ]
            if rec.get("summary", "").strip():
                lines += ["", f"Summary: {rec['summary'].strip()}"]
            for field in ("keywords", "features", "workflows", "personas", "entities"):
                vals = rec.get(field) or []
                if vals:
                    lines.append(f"{field.capitalize()}: {', '.join(vals)}")
            lines.append("")
            return lines

        lines: list[str] = [
            f"# window {win_idx} of {total_windows}  ({len(recs)} blocks)\n"
        ]
        for rec in recs:
            lines.extend(_block_lines(rec))

        with self._stage3_path(doc_id).open("a", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        logger.debug(
            "stage3_content_all.txt  appended window %d/%d  blocks=%d",
            win_idx, total_windows, len(recs),
        )

    def _dump_blocks(self, blocks: list["Chunk"], doc_id: str) -> None:
        """Write LLM-extracted blocks (before recursive re-chunking) to uploads/<doc_id>/.

        Files written
        ─────────────
        stage3_blocks.jsonl              — full structured record per block
        stage3_blocks_summary.json       — counts by type + empty-content tally
        stage3_content_<type>.txt        — plain-text content for every block of
                                           that type (knowledge/keywords/entities/
                                           features/workflows/personas), one entry
                                           per block separated by a ruled divider
        """
        import json as _json
        from collections import Counter as _Counter

        dump_dir = Path(self.settings.upload_dir) / doc_id
        dump_dir.mkdir(parents=True, exist_ok=True)

        records = []
        for b in blocks:
            records.append({
                "chunk_id":    b.chunk_id,
                "type":        b.metadata.chunk_type.value,
                "sub_type":    b.metadata.sub_type,
                "name":        b.metadata.headings[0] if b.metadata.headings else "",
                "window":      b.metadata.headings[1] if len(b.metadata.headings) > 1 else "",
                "depth":       b.metadata.depth,
                "is_leaf":     b.metadata.is_leaf,
                "parent_id":   b.metadata.parent_id,
                "content":     b.content,
                "summary":     b.summary,
                "keywords":    b.keywords,
                "features":    b.features,
                "workflows":   b.workflows,
                "personas":    b.personas,
                "entities":    b.entities,
                "token_count": b.token_count,
            })

        # ── stage3_blocks.jsonl ───────────────────────────────────────────────
        blocks_path = dump_dir / "stage3_blocks.jsonl"
        with blocks_path.open("w", encoding="utf-8") as fh:
            for rec in records:
                fh.write(_json.dumps(rec, ensure_ascii=False) + "\n")

        # ── stage3_blocks_summary.json ────────────────────────────────────────
        by_type = dict(_Counter(r["type"] for r in records).most_common())
        summary_path = dump_dir / "stage3_blocks_summary.json"
        summary_path.write_text(_json.dumps({
            "doc_id":        doc_id,
            "total_blocks":  len(records),
            "by_type":       by_type,
            "empty_content": sum(1 for r in records if not r["content"].strip()),
        }, indent=2), encoding="utf-8")

        # ── stage3_content_<type>.txt — one file per block type ───────────────
        # Group records by type, preserving window order (records are already
        # ordered by extraction sequence).
        by_type_records: dict[str, list[dict]] = {}
        for rec in records:
            by_type_records.setdefault(rec["type"], []).append(rec)

        DIVIDER = "─" * 72

        def _block_lines(rec: dict) -> list[str]:
            """Return the human-readable lines for a single block."""
            lines = [
                DIVIDER,
                f"[{rec['type'].upper()}]  {rec['name']}"
                f"  |  sub_type={rec['sub_type']}"
                f"  |  {rec['window']}"
                f"  |  tokens={rec['token_count']}",
                "",
                rec["content"].strip() or "(empty)",
            ]
            if rec["summary"].strip():
                lines += ["", f"Summary: {rec['summary'].strip()}"]
            for field in ("keywords", "features", "workflows", "personas", "entities"):
                vals = rec.get(field) or []
                if vals:
                    lines.append(f"{field.capitalize()}: {', '.join(vals)}")
            lines.append("")
            return lines

        for block_type, type_records in by_type_records.items():
            lines: list[str] = [
                f"# Stage-3 extracted content — type: {block_type}",
                f"# doc_id : {doc_id}",
                f"# blocks : {len(type_records)}",
                "",
            ]
            for rec in type_records:
                lines.extend(_block_lines(rec))

            content_path = dump_dir / f"stage3_content_{block_type}.txt"
            content_path.write_text("\n".join(lines), encoding="utf-8")
            logger.info(
                "DEBUG dump: stage3_content_%s.txt (%d blocks)  → %s",
                block_type, len(type_records), dump_dir,
            )

        # ── stage3_content_all.txt — every block in window order ─────────────
        # Single file with ALL blocks in extraction sequence so you can read
        # the full pipeline output in one place.
        all_lines: list[str] = [
            f"# Stage-3 extracted content — ALL blocks",
            f"# doc_id : {doc_id}",
            f"# blocks : {len(records)}",
            f"# types  : {', '.join(f'{t}={n}' for t, n in by_type.items())}",
            "",
        ]
        for rec in records:
            all_lines.extend(_block_lines(rec))

        all_path = dump_dir / "stage3_content_all.txt"
        all_path.write_text("\n".join(all_lines), encoding="utf-8")

        logger.info(
            "DEBUG dump: stage3_content_all.txt (%d blocks) + per-type .txt files  → %s",
            len(records), dump_dir,
        )
        logger.info(
            "DEBUG dump: stage3_blocks.jsonl (%d blocks  by_type=%s)  → %s",
            len(records), by_type, dump_dir,
        )
