"""
Pipeline helpers — RAW.md builder, concise builder, and knowledge-context reader.

These are the glue functions that connect the classifier output to the final
*.md files written per ingestion run.
"""
from __future__ import annotations

from pathlib import Path

from src.enums import ChunkCategory
from src.services.ingestion.prompts import (
    SYSTEM_PROMPTS  as _CONCISE_SYSTEM_PROMPTS,
    COMPRESS_SYSTEM as _COMPRESS_SYSTEM,
)
from .helpers import _today


def _build_raw_md(
    records: list[dict],
    category: str,
    doc_name: str,
    pdf_name: str,
) -> str:
    """
    Write one ## section per chunk containing ONLY:
      - heading path
      - chunk_id
      - LLM-generated summary  (or extractive fallback label)

    No verbatim content — the *_RAW.md is a pure summary index that the
    Phase 2 LLM can consume efficiently.
    """
    ordered = sorted(
        records,
        key=lambda r: (r.get("depth", 0), -r.get("token_count", 0)),
    )
    lines = [
        f"# {doc_name} — {category.upper()} Summaries",
        "",
        f"**Source:** {pdf_name}",
        f"**Category:** {category}",
        f"**Total entries:** {len(ordered)}",
        f"**Export Date:** {_today()}",
        "",
        "---",
        "",
    ]
    for seq, r in enumerate(ordered, 1):
        headings     = r.get("headings") or []
        heading_path = " > ".join(h.replace("\n", " ").strip() for h in headings if h.strip())
        chunk_id     = r.get("chunk_id", "")
        summary      = (r.get("summary") or "").strip()
        cats         = ", ".join(r.get("categories") or [category])

        lines += [
            f"## {seq}. {heading_path or '(no heading)'}",
            "",
            f"`{chunk_id}`  |  **categories:** {cats}",
            "",
            summary if summary else "*(no summary — extractive fallback)*",
            "",
            "---",
            "",
        ]
    return "\n".join(lines)


def _build_knowledge_context(summary_dir: Path, max_chars_each: int = 2000) -> str:
    """Read the already-written *.md files (non-knowledge) from summary_dir
    and stitch them into a context string for the KNOWLEDGE master pass."""
    parts: list[str] = []
    for cat in (
        ChunkCategory.FEATURES.value,
        ChunkCategory.WORKFLOWS.value,
        ChunkCategory.ENTITIES.value,
        ChunkCategory.KEYWORDS.value,
        ChunkCategory.PERSONAS.value,
    ):
        p = summary_dir / f"{cat.upper()}.md"
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore").strip()
        idx = text.find("\n---\n")
        body = text[idx + 5:].strip() if idx >= 0 else text
        if body:
            parts.append(f"[{cat.upper()}]\n{body[:max_chars_each]}")
    return "\n\n".join(parts)


def _build_concise_from_raw(
    raw_text: str,
    category: str,
    doc_name: str,
    pdf_name: str,
    llm,                          # LLMService instance
    extra_context: str = "",
) -> str:
    """
    Two-layer LLM summarisation used for KNOWLEDGE (other categories batch
    their requests directly in generate() for maximum concurrency).

    Layer 1: RAW → structured Markdown  (4000-char segments)
    Layer 2: structured → compressed final  (6000-char windows)
    Falls back to first 8000 chars of raw_text when LLM is disabled.
    """
    header = "\n".join([
        f"# {doc_name} — {category.upper()}",
        "",
        f"**Category:** {category}  |  **Generated:** {_today()}  "
        f"|  **Source:** {pdf_name}",
        "",
        "---",
        "",
    ])

    if not llm.enabled:
        return header + raw_text[:8000]

    layer1_sys = _CONCISE_SYSTEM_PROMPTS.get(category) or (
        "Produce a single well-structured Markdown document from the raw summaries. "
        "Group related items under ## headings. De-duplicate near-identical entries. "
        "Output ONLY the Markdown."
    )
    seg_size = 4000
    segments = [raw_text[i : i + seg_size] for i in range(0, len(raw_text), seg_size)]
    if extra_context:
        segments[0] = f"CONTEXT (from other category files — use for overview only):\n{extra_context[:3000]}\n\n---\n\n{segments[0]}"
    l1_resps = llm.complete_batch([(layer1_sys, seg) for seg in segments])
    l1_body  = "\n\n".join(r.strip() for r in l1_resps if r.strip())

    if not l1_body:
        return header + raw_text[:8000]

    win_size = 6000
    l1_wins  = [l1_body[i : i + win_size] for i in range(0, len(l1_body), win_size)]
    l2_resps = llm.complete_batch([(_COMPRESS_SYSTEM, w) for w in l1_wins])
    l2_body  = "\n\n".join(r.strip() for r in l2_resps if r.strip())

    return header + (l2_body or l1_body)
