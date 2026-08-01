"""
Chunk Summary Pipeline
══════════════════════

Two-phase pipeline per category (features, workflows, personas, knowledge,
entities, keywords):

  Phase 1 — RAW  : summarize every chunk via AIM in concurrent windows of 16.
                   Write <CATEGORY>_RAW.md (one section per chunk, verbatim +
                   LLM summary appended).

  Phase 2 — CONCISE : send the RAW summaries back to AIM and produce a single
                      cohesive <CATEGORY>.md (de-duplicated, structured markdown).

Usage
─────
    from src.services.ingestion.chunk_summary_pipeline import ChunkSummaryPipeline

    pipeline = ChunkSummaryPipeline()
    pipeline.run(
        chunks_by_category={"features": [...], "knowledge": [...]},
        out_dir=Path("output/my-doc"),
        source_name="my-doc",
    )

    # Or stand-alone from CLI:
    python -m src.services.ingestion.chunk_summary_pipeline \\
        --jsonl output/my-doc/chunks_features.jsonl \\
        --category features \\
        --out output/my-doc

Concurrency
───────────
Benchmarks (see llm_service.py benchmarks) confirm 32 simultaneous curl calls
succeed with ~2.6s wall time and 0 failures.  We use windows of 16 to leave
WAF headroom — 227 summarizer requests collapse from ~4 min → ~28s.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

from src.utils.llm_helpers import _make_snippet, _parse_blocks

logger = logging.getLogger(__name__)


def _get_defaults() -> tuple[str, str, str]:
    """Read AIM endpoint config from settings (env / .env file)."""
    try:
        from src.config.settings import get_settings
        s = get_settings()
        return s.llm_base_url, s.llm_api_key, s.llm_model
    except Exception:
        # Fall back to env vars directly so the CLI still works without a full settings stack
        url   = os.environ.get("LLM_BASE_URL", "")
        key   = os.environ.get("LLM_API_KEY", "")
        model = os.environ.get("LLM_MODEL", "")
        return url, key, model


# Window size proven safe from concurrent benchmark (32 OK → use 16 for margin)
_WINDOW = 16
_MAX_TOKENS = 1000   # model caps at ~94 completion tokens regardless; 1000 is safe

# ── Per-category prompts ──────────────────────────────────────────────────────

_RAW_SYSTEM: dict[str, str] = {
    "features": (
        "You are a precise technical analyst. For each numbered excerpt, extract "
        "the feature described. Replace N with the actual excerpt number.\n"
        "Output ONLY blocks in this exact form — one per excerpt:\n\n"
        "===1===\n"
        "- Name: <exact feature name>\n"
        "- Description: <2-3 complete sentences: what it does, how, key benefit>\n"
        "- Keywords: <6-8 product-specific terms, comma-separated>\n\n"
        "===2===\n"
        "- Name: ...\n"
        "...\n\n"
        "Output ONLY the ===number=== blocks. Nothing else."
    ),
    "workflows": (
        "You are a precise technical analyst. Classify each excerpt as "
        "navigation | configuration | action. Replace N with the excerpt number.\n"
        "Output ONLY blocks in this exact form — one per excerpt:\n\n"
        "===1===\n"
        "- Name: <workflow name>\n"
        "- Type: <navigation | configuration | action>\n"
        "- Steps: <numbered steps from the excerpt text>\n\n"
        "===2===\n"
        "- Name: ...\n"
        "...\n\n"
        "Output ONLY the ===number=== blocks. Nothing else."
    ),
    "personas": (
        "You are a precise technical analyst. Identify the user role implied. "
        "Use: Database Administrator, Security Administrator, Compliance Officer, "
        "Application Developer, DevOps Engineer, Data Analyst, Security Analyst, "
        "Compliance Auditor, IT Manager, Administrator, Operator.\n"
        "Replace N with the actual excerpt number.\n"
        "Output ONLY blocks in this exact form — one per excerpt:\n\n"
        "===1===\n"
        "- Persona: <role archetype>\n"
        "- Responsibilities: <2-3 specific responsibilities from the excerpt>\n"
        "- Features used: <product features this persona operates>\n\n"
        "===2===\n"
        "- Persona: ...\n"
        "...\n\n"
        "Output ONLY the ===number=== blocks. Nothing else."
    ),
    "knowledge": (
        "You are a precise technical analyst. Synthesize a knowledge topic. "
        "Replace N with the actual excerpt number.\n"
        "Output ONLY blocks in this exact form — one per excerpt:\n\n"
        "===1===\n"
        "- Topic: <concept name from the heading>\n"
        "- Summary: <3-5 complete sentences: what it is, how it works, why it matters>\n"
        "- Keywords: <8-12 product-specific terms, comma-separated>\n\n"
        "===2===\n"
        "- Topic: ...\n"
        "...\n\n"
        "Output ONLY the ===number=== blocks. Nothing else."
    ),
    "entities": (
        "You are a precise technical analyst. Extract the named system object. "
        "Replace N with the actual excerpt number.\n"
        "Output ONLY blocks in this exact form — one per excerpt:\n\n"
        "===1===\n"
        "- Name: <entity name>\n"
        "- Type: <policy|agent|node|service|database|api|credential|tool|report|component|other>\n"
        "- Description: <2-3 complete sentences: what this object is and does>\n\n"
        "===2===\n"
        "- Name: ...\n"
        "...\n\n"
        "Output ONLY the ===number=== blocks. Nothing else."
    ),
    "keywords": (
        "You are a precise technical analyst. Extract product-specific terms only. "
        "Replace N with the actual excerpt number.\n"
        "Output ONLY blocks in this exact form — one per excerpt:\n\n"
        "===1===\n"
        "- Term: <product-specific term or acronym — exact casing>\n"
        "- Expansion: <full form; repeat term if not an acronym>\n"
        "- Definition: <one complete sentence: what it IS and does in the product>\n\n"
        "===2===\n"
        "- Term: ...\n"
        "...\n\n"
        "Output ONLY the ===number=== blocks. Nothing else."
    ),
}

_CONCISE_SYSTEM = (
    "You are a precise technical writer. Below are raw chunk summaries for the "
    "'{category}' category of a product documentation set.\n\n"
    "Produce a single well-structured Markdown document:\n"
    "- De-duplicate near-identical entries (keep the richest version)\n"
    "- Group related items under H2 headings\n"
    "- Use bullet lists for properties (Name, Description, Keywords, etc.)\n"
    "- Keep language concise and technical — no filler prose\n"
    "- Preserve all distinct product-specific terminology\n\n"
    "Output ONLY the Markdown content. No preamble, no meta-commentary."
)


# ── Low-level AIM caller ──────────────────────────────────────────────────────

def _curl_call(url: str, api_key: str, model: str,
               system: str, user: str, max_tokens: int,
               timeout: int = 60) -> str:
    """Synchronous curl call. Returns response text or '' on failure."""
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
        "max_tokens": max_tokens,
    })
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        tmp.write(body)
        tmp_path = tmp.name
    try:
        r = subprocess.run(
            ["/usr/bin/curl", "-s", "-X", "POST", url,
             "-H", f"Authorization: Bearer {api_key}",
             "-H", "Content-Type: application/json",
             "-H", "Accept: application/json",
             "-d", f"@{tmp_path}",
             "--max-time", str(timeout)],
            capture_output=True, text=True, timeout=timeout + 5,
        )
    finally:
        os.unlink(tmp_path)

    if r.returncode != 0 or not r.stdout.strip():
        logger.warning("curl failed: rc=%d  stderr=%s", r.returncode, r.stderr[:120])
        return ""
    raw = r.stdout.strip()
    if raw.lstrip().startswith("<"):
        logger.warning("WAF HTML block received — returning empty")
        return ""
    try:
        d = json.loads(raw)
        if "choices" in d:
            return d["choices"][0]["message"]["content"].strip()
        logger.warning("AIM error response: %s", raw[:200])
    except Exception as e:
        logger.warning("JSON parse error: %s  raw=%s", e, raw[:120])
    return ""


async def _concurrent_window(
    url: str, api_key: str, model: str,
    requests: list[tuple[str, str]],   # (system, user)
    max_tokens: int,
    timeout: int,
) -> list[str]:
    """Fire all requests in the window concurrently via asyncio + executor."""
    loop = asyncio.get_event_loop()
    tasks = [
        loop.run_in_executor(None, _curl_call, url, api_key, model, sys, usr, max_tokens, timeout)
        for sys, usr in requests
    ]
    return list(await asyncio.gather(*tasks))


def _run_batched(
    url: str, api_key: str, model: str,
    requests: list[tuple[str, str]],
    max_tokens: int = _MAX_TOKENS,
    window: int = _WINDOW,
    inter_window_delay: float = 1.0,
    timeout: int = 60,
) -> list[str]:
    """
    Fire requests in sliding windows of `window` concurrent calls.
    Returns results list parallel to requests.
    """
    results: list[str] = []
    windows = [requests[i : i + window] for i in range(0, len(requests), window)]
    for w_idx, win in enumerate(windows):
        if w_idx > 0 and inter_window_delay > 0:
            time.sleep(inter_window_delay)
        batch_results = asyncio.run(
            _concurrent_window(url, api_key, model, win, max_tokens, timeout)
        )
        results.extend(batch_results)
        filled = sum(1 for r in batch_results if r)
        logger.info(
            "  window %d/%d  filled=%d/%d",
            w_idx + 1, len(windows), filled, len(win),
        )
    return results


# ── Helpers ───────────────────────────────────────────────────────────────────

def _today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _chunks_per_batch(category: str) -> int:
    """Tune excerpts per LLM request by category verbosity."""
    return {"keywords": 10, "personas": 10}.get(category, 15)


# ══════════════════════════════════════════════════════════════════════════════
# Main pipeline class
# ══════════════════════════════════════════════════════════════════════════════

class ChunkSummaryPipeline:
    """
    Orchestrates two-phase summarisation:
      Phase 1: chunks → AIM → *_RAW.md  (one LLM summary per chunk)
      Phase 2: RAW summaries → AIM → *.md  (concise, de-duplicated document)
    """

    def __init__(
        self,
        aim_url:   Optional[str] = None,
        api_key:   Optional[str] = None,
        model:     Optional[str] = None,
        max_tokens: int = _MAX_TOKENS,
        window:    int = _WINDOW,
        inter_window_delay: float = 1.0,
        timeout:   int = 60,
    ):
        _url, _key, _mdl = _get_defaults()
        self._url     = aim_url or _url
        self._key     = api_key or _key
        self._model   = model   or _mdl
        self._max_tok = max_tokens
        self._window  = window
        self._delay   = inter_window_delay
        self._timeout = timeout

    # ── Phase 1: chunks → *_RAW.md ───────────────────────────────────────────

    def summarize_chunks(
        self,
        category: str,
        chunks: list[dict],
        out_dir: Path,
        source_name: str,
    ) -> Path:
        """
        Summarize every chunk for `category` via AIM and write <CATEGORY>_RAW.md.
        Returns the path written.
        """
        system  = _RAW_SYSTEM.get(category, _RAW_SYSTEM["knowledge"])
        bsize   = _chunks_per_batch(category)
        batches = [chunks[i : i + bsize] for i in range(0, len(chunks), bsize)]

        logger.info(
            "[Phase-1] %s  chunks=%d  batches=%d  window=%d",
            category.upper(), len(chunks), len(batches), self._window,
        )

        # Build one (system, user) pair per batch
        requests: list[tuple[str, str]] = []
        for batch in batches:
            lines = [
                f"--- Excerpt {seq} ---\n{_make_snippet(c)}"
                for seq, c in enumerate(batch, 1)
            ]
            requests.append((system, "\n\n".join(lines)))

        # Fire all requests in concurrent windows
        t0 = time.time()
        raw_responses = _run_batched(
            self._url, self._key, self._model,
            requests,
            max_tokens=self._max_tok,
            window=self._window,
            inter_window_delay=self._delay,
            timeout=self._timeout,
        )
        elapsed = time.time() - t0

        # Parse + build RAW md
        lines_md: list[str] = [
            f"# {source_name} — {category.upper()} RAW Summaries",
            "",
            f"**Category:** {category}  |  **Chunks:** {len(chunks)}  "
            f"|  **Generated:** {_today()}  |  **Elapsed:** {elapsed:.1f}s",
            "",
            "---",
            "",
        ]

        total_filled = 0
        for batch, raw in zip(batches, raw_responses):
            parsed = _parse_blocks(raw, len(batch)) if raw else [""] * len(batch)
            for chunk, summary in zip(batch, parsed):
                headings = chunk.get("headings") or chunk.get("metadata", {}).get("headings") or []
                path     = " > ".join(h.replace("\n"," ").strip() for h in headings if h.strip())
                body     = re.sub(r"\s+", " ", chunk.get("content","").strip())[:500]
                chunk_id = chunk.get("chunk_id", chunk.get("id", ""))

                lines_md += [f"## {path or '(no heading)'}", ""]
                if chunk_id:
                    lines_md += [f"`{chunk_id}`", ""]
                lines_md += [
                    "**Verbatim excerpt:**",
                    f"> {body}",
                    "",
                ]
                if summary.strip():
                    total_filled += 1
                    lines_md += [
                        "**LLM Summary:**",
                        summary.strip(),
                        "",
                    ]
                else:
                    lines_md += ["**LLM Summary:** *(extractive fallback)*", ""]
                lines_md += ["---", ""]

        lines_md.append(
            f"*Filled: {total_filled}/{len(chunks)} chunks with LLM summaries*"
        )

        out_path = out_dir / f"{category.upper()}_RAW.md"
        out_path.write_text("\n".join(lines_md), encoding="utf-8")
        logger.info(
            "[Phase-1] Written %s  filled=%d/%d  elapsed=%.1fs",
            out_path.name, total_filled, len(chunks), elapsed,
        )
        return out_path

    # ── Phase 2: *_RAW.md → concise *.md ─────────────────────────────────────

    def generate_concise(
        self,
        category: str,
        raw_md_path: Path,
        out_dir: Path,
        source_name: str,
    ) -> Path:
        """
        Read <CATEGORY>_RAW.md, send it to AIM in chunks (4000-char windows),
        and produce a concise, de-duplicated <CATEGORY>.md.
        """
        raw_text = raw_md_path.read_text(encoding="utf-8")
        system   = _CONCISE_SYSTEM.replace("{category}", category)

        # Chunk the raw text into 4000-char segments to stay within context window
        seg_size = 4000
        segments = [raw_text[i : i + seg_size] for i in range(0, len(raw_text), seg_size)]

        logger.info(
            "[Phase-2] %s  raw_chars=%d  segments=%d",
            category.upper(), len(raw_text), len(segments),
        )

        requests = [(system, seg) for seg in segments]
        t0 = time.time()
        responses = _run_batched(
            self._url, self._key, self._model,
            requests,
            max_tokens=self._max_tok,
            window=self._window,
            inter_window_delay=self._delay,
            timeout=self._timeout,
        )
        elapsed = time.time() - t0

        header = "\n".join([
            f"# {source_name} — {category.upper()}",
            "",
            f"**Category:** {category}  |  **Generated:** {_today()}  "
            f"|  **Source:** {raw_md_path.name}",
            "",
            "---",
            "",
        ])
        body = "\n\n---\n\n".join(r for r in responses if r.strip())
        out_path = out_dir / f"{category.upper()}.md"
        out_path.write_text(header + body, encoding="utf-8")
        logger.info(
            "[Phase-2] Written %s  elapsed=%.1fs",
            out_path.name, elapsed,
        )
        return out_path

    # ── Orchestrator ──────────────────────────────────────────────────────────

    def run(
        self,
        chunks_by_category: dict[str, list[dict]],
        out_dir: Path,
        source_name: str,
    ) -> dict[str, tuple[Path, Path]]:
        """
        Run both phases for every category in chunks_by_category.

        Returns:
            {category: (raw_md_path, concise_md_path)}
        """
        out_dir.mkdir(parents=True, exist_ok=True)
        results: dict[str, tuple[Path, Path]] = {}

        for category, chunks in chunks_by_category.items():
            if not chunks:
                logger.info("Skipping empty category: %s", category)
                continue
            logger.info("=== Processing category: %s (%d chunks) ===", category, len(chunks))
            raw_path = self.summarize_chunks(category, chunks, out_dir, source_name)
            concise_path = self.generate_concise(category, raw_path, out_dir, source_name)
            results[category] = (raw_path, concise_path)

        return results


# ── CLI entry point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse, sys

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    parser = argparse.ArgumentParser(
        description="Run chunk summary pipeline on a JSONL file."
    )
    parser.add_argument("--jsonl",    required=True,  help="Path to chunks JSONL file")
    parser.add_argument("--category", required=True,  help="Category name (features, knowledge, ...)")
    parser.add_argument("--out",      required=True,  help="Output directory")
    parser.add_argument("--source",   default="doc",  help="Source name for headings")
    parser.add_argument("--window",   type=int, default=_WINDOW,  help=f"Concurrent window size (default {_WINDOW})")
    parser.add_argument("--delay",    type=float, default=1.0, help="Inter-window delay seconds (default 1.0)")
    args = parser.parse_args()

    jsonl_path = Path(args.jsonl)
    if not jsonl_path.exists():
        print(f"ERROR: {jsonl_path} not found", file=sys.stderr)
        sys.exit(1)

    chunks: list[dict] = []
    with jsonl_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))

    print(f"Loaded {len(chunks)} chunks from {jsonl_path}")

    pipeline = ChunkSummaryPipeline(window=args.window, inter_window_delay=args.delay)
    out_dir  = Path(args.out)
    results  = pipeline.run(
        {args.category: chunks},
        out_dir=out_dir,
        source_name=args.source,
    )

    for cat, (raw, concise) in results.items():
        print(f"\n  RAW     → {raw}")
        print(f"  CONCISE → {concise}")
