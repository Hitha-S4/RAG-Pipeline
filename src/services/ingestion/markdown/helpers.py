"""
Low-level, stateless text-processing helpers used across the markdown package.
No LLM dependencies — pure Python only.
"""
from __future__ import annotations

import re
from collections import Counter
from datetime import datetime
from pathlib import Path


# ── Constants ─────────────────────────────────────────────────────────────────

MAX_RAW_BODY      = 300   # chars per entry — tuned for 8B model context budget
DOC_NAME_FALLBACK = "Documentation"


# ── Helpers ───────────────────────────────────────────────────────────────────

def _today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _clean_title(text: str) -> str:
    """Fix OCR spacing artifacts in heading names (e.g. 'Doc ument' → 'Document')."""
    text = re.sub(r"(?<=[A-Za-z]{2}) (?=[a-z])", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _clean_body(text: str, max_chars: int = MAX_RAW_BODY) -> str:
    """Collapse whitespace and strip any legacy parent prefixes."""
    text = re.sub(r"^\[Parent[^\]]*\]\n\n", "", text, flags=re.DOTALL)
    text = re.sub(r"^#+\s.*?\n\n", "", text, flags=re.DOTALL)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_chars:
        cut  = text[:max_chars]
        last = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
        text = (text[:last + 1] if last > max_chars // 2 else cut).strip()
    return text


def _extract_keywords(text: str, top_n: int = 12) -> list[str]:
    stop = {
        "the","a","an","and","or","of","for","in","to","on","with","by","is","are",
        "was","were","be","been","being","have","has","had","do","does","did","will",
        "would","could","should","may","might","this","that","these","those","it","its",
        "you","your","we","our","they","their","he","she","his","her","at","from","as",
        "into","if","when","then","so","but","not","can","all","more","also","such",
        "each","any","which","who","how","what","where","about","use","used","using",
        "click","select","enter","open","see",
    }
    words = re.findall(r"\b[a-zA-Z][a-zA-Z0-9\-]{2,}\b", text)
    counts: Counter = Counter(w.lower() for w in words if w.lower() not in stop)
    return [w for w, _ in counts.most_common(top_n)]


def _heading_label(chunk: dict, max_len: int = 80) -> str:
    headings = chunk.get("headings") or []
    label    = headings[-1] if headings else chunk.get("chunk_id", "Untitled")
    label    = label.replace("\n", " ").strip()
    return label[:max_len] + ("…" if len(label) > max_len else "")


def _source_section(chunk: dict) -> str:
    """Return the L1 heading as the 'Source Section' label."""
    headings = chunk.get("headings") or []
    return headings[0].replace("\n", " ").strip() if headings else "General"


def _skip_noise(text: str) -> bool:
    s = text.strip()
    if s.startswith("[") and s.endswith("]") and len(s) < 120:
        return True
    return bool(re.search(
        r"[A-Z_]{4,}\s*\|\s*[A-Z_]{4,}|^\s*[\d\.\-]+\s*$",
        text, re.MULTILINE,
    ))


def _best_entries(chunks: list[dict], max_n: int = 50) -> list[dict]:
    """Deduplicated parent-level (non-leaf preferred) or leaf chunks, richest first."""
    seen: set[str] = set()
    result = []
    ordered = sorted(
        chunks,
        key=lambda c: (int(c.get("is_leaf", True)), -c.get("token_count", 0)),
    )
    for c in ordered:
        if _skip_noise(c.get("content", "")):
            continue
        label = _heading_label(c)
        if label in seen:
            continue
        body = _clean_body(c.get("content", ""))
        if len(body) < 8:
            continue
        seen.add(label)
        result.append(c)
        if len(result) >= max_n:
            break
    return result


def _file_header(doc_name: str, chunk_type: str, pdf_name: str,
                 generation_method: str) -> list[str]:
    return [
        f"# {doc_name} — {chunk_type} Chunk Export",
        "",
        f"**Generated From:** {doc_name}",
        f"**Chunk Type:** {chunk_type}",
        f"**Export Date:** {_today()}",
        f"**Generation Method:** {generation_method}",
        "",
        "---",
        "",
    ]


def _normalise_heading(label: str) -> str:
    """
    Strip numeric page-number suffixes appended by the chunker, e.g.
    'Some Document Title 453' → 'Some Document Title'.
    Only strips a trailing integer that is preceded by a letter (not "PKCS 12").
    """
    label = re.sub(r"(?<=[A-Za-z])\s+\d+\s*$", "", label).strip()
    return label
