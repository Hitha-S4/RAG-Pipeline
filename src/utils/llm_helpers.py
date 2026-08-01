"""
Shared parse/format helpers used by both LLMService and ClassifyService.
"""
from __future__ import annotations

import re


def _is_placeholder(content: str) -> bool:
    """True for content that is just [Heading text] — nothing for the LLM to extract."""
    s = content.strip()
    return (s.startswith("[") and s.endswith("]")) or len(s) < 15


def _make_snippet(chunk: dict, max_chars: int = 300) -> str:
    """
    Build the excerpt text sent to the LLM.
    Heading path prepended so short/placeholder-adjacent chunks have context.
    Content stripped of parent-prefix boilerplate.
    """
    headings = chunk.get("headings") or []
    path = " > ".join(h.replace("\n", " ").strip() for h in headings if h.strip())

    body = chunk.get("content", "").strip()
    body = re.sub(r"^\[Parent[^\]]*\]\n\n", "", body, flags=re.DOTALL)
    body = re.sub(r"^#+\s.*?\n\n", "", body, flags=re.DOTALL)
    body = re.sub(r"\s+", " ", body).strip()

    if len(body) > max_chars:
        cut  = body[:max_chars]
        last = max(cut.rfind(". "), cut.rfind("? "))
        body = (body[:last + 1] if last > max_chars // 2 else cut).strip()

    return f"[{path}]\n{body}" if body and not _is_placeholder(body) else f"[{path}]"


def _parse_blocks(response: str, n: int) -> list[str]:
    """
    Split on ===N=== markers. Returns list of length n (empty string = no block).
    Tolerates minor whitespace/quote variants the model may produce.
    """
    results = [""] * n
    parts = re.split(r"={2,}\s*(\d+)\s*[=:]{1,3}", response)
    i = 1
    while i + 1 < len(parts):
        try:
            idx = int(parts[i].strip()) - 1
            if 0 <= idx < n:
                results[idx] = parts[i + 1].strip()
        except ValueError:
            pass
        i += 2
    return results
