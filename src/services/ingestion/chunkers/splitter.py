"""
Recursive character text splitter — LangChain-style hierarchical splitting with
token-budgeted windows and sliding overlap.

Why this exists
───────────────
The old `_split_by_budget` in chunker.py split on paragraphs, then sentences,
and stopped there — with **no overlap** and no word-level fallback. A single
run-on paragraph with no sentence punctuation (very common in PDF table dumps
and OCR output) could therefore blow straight past the ceiling, and adjacent
chunks shared no context, hurting retrieval recall at chunk boundaries.

This module fixes both:

  1. Hierarchical separators, tried in order until a piece fits the budget:
         paragraphs ("\n\n")  →  lines ("\n")  →  sentences  →  words (" ")  →  chars
     (mirrors RecursiveCharacterTextSplitter semantics).

  2. Sliding-window overlap measured in *tokens* (default 10-15 % of chunk size),
     so consecutive chunks re-share their tail→head context.

Token counting is pluggable. By default it reuses the same char/token heuristic
the rest of the codebase uses (settings.chars_per_token) so behaviour is
consistent, but you can pass any `len_fn` (e.g. a real tokenizer's encode-len)
for exact budgeting.

Usage
─────
    from src.services.ingestion.chunkers.splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,          # target tokens per chunk
        chunk_overlap=64,        # ~12.5 % overlap (50-75 recommended)
        chars_per_token=4.5,
    )
    pieces = splitter.split_text(long_text)
"""
from __future__ import annotations

import re
from typing import Callable, List, Optional

# Matches the end of a sentence — used to detect fragments that are
# *complete* sentences so we can avoid starting a new chunk with one.
_TERMINAL_PUNCT = re.compile(r"[.!?]\s*$")

# Default separator ladder — coarse → fine. The empty string at the end means
# "split on individual characters" as an absolute last resort.
#
# NOTE: "\n" (single newline) is placed AFTER the sentence terminators ". ? ! ;"
# deliberately.  If it came before them, a sentence that wraps across two lines:
#     "This is a long sentence that\nspans two lines."
# would be split on the newline first — producing fragment "This is a long sentence that"
# and "spans two lines." — which could land in different chunks, cutting mid-sentence.
# Paragraph breaks ("\n\n") are still tried first because they are structurally
# stronger than sentence boundaries.
_DEFAULT_SEPARATORS: tuple[str, ...] = ("\n\n", ". ", "? ", "! ", "; ", "\n", " ", "")

# Sentence-boundary regex used when we split on the ". " family so we do not cut
# common abbreviations (e.g. "e.g.", "Inc.") in the middle.
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z(0-9\"'])")


def default_token_len(text: str, chars_per_token: float = 4.5) -> int:
    """Approximate token count using the project-wide char/token heuristic."""
    return max(1, int(len(text) / chars_per_token))


class RecursiveCharacterTextSplitter:
    """
    Split text into ~chunk_size-token windows with chunk_overlap-token overlap,
    recursively backing off to finer separators when a piece is too large.

    Parameters
    ----------
    chunk_size      : target tokens per chunk (soft target, hard-capped at this)
    chunk_overlap   : tokens of overlap between consecutive chunks
    separators      : ordered list of separators, coarse → fine
    chars_per_token : heuristic used by the default length function
    len_fn          : custom token-length function; overrides chars_per_token
    keep_separator  : re-attach the separator to the preceding piece (keeps
                      sentence punctuation etc.)
    """

    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 64,
        separators: Optional[List[str]] = None,
        chars_per_token: float = 4.5,
        len_fn: Optional[Callable[[str], int]] = None,
        keep_separator: bool = True,
    ):
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be smaller than chunk_size")
        self.chunk_size     = chunk_size
        self.chunk_overlap  = chunk_overlap
        self.separators     = list(separators) if separators else list(_DEFAULT_SEPARATORS)
        self.keep_separator = keep_separator
        self._len = len_fn or (lambda t: default_token_len(t, chars_per_token))

    # ── Public API ────────────────────────────────────────────────────────────

    def split_text(self, text: str) -> List[str]:
        """Return a list of overlapping chunks, each ≤ chunk_size tokens."""
        text = text.strip()
        if not text:
            return []
        splits = self._recursive_split(text, self.separators)
        # _recursive_split yields atomic, under-budget fragments; now pack them
        # into windows with overlap.
        return self._merge_with_overlap(splits)

    # ── Recursive splitting ───────────────────────────────────────────────────

    def _recursive_split(self, text: str, separators: List[str]) -> List[str]:
        """
        Break `text` into fragments that individually fit the budget, using the
        finest separator necessary. Returns fragments in document order.
        """
        if self._len(text) <= self.chunk_size:
            return [text] if text.strip() else []

        # Find the first separator that actually occurs in the text.
        sep = separators[-1]
        rest = separators[1:]
        for i, s in enumerate(separators):
            if s == "":
                sep = s
                rest = separators[i + 1:]
                break
            if s in text:
                sep = s
                rest = separators[i + 1:]
                break

        pieces = self._split_on(text, sep)

        out: List[str] = []
        for piece in pieces:
            if not piece.strip():
                continue
            if self._len(piece) <= self.chunk_size:
                out.append(piece)
            elif rest:
                out.extend(self._recursive_split(piece, rest))
            else:
                # No finer separator left — hard-split by character budget.
                out.extend(self._hard_char_split(piece))
        return out

    def _split_on(self, text: str, sep: str) -> List[str]:
        """Split on a separator, optionally re-attaching it to each piece."""
        if sep == "":
            return list(text)  # character-level
        if sep in (". ", "? ", "! ", "; "):
            # Sentence-aware split so abbreviations survive.
            parts = _SENTENCE_RE.split(text)
            return [p for p in parts if p]
        if not self.keep_separator:
            return [p for p in text.split(sep) if p]
        # Keep the separator attached to the left piece.
        chunks = text.split(sep)
        out = [chunks[0]] if chunks else []
        for c in chunks[1:]:
            out.append(sep + c if sep == "\n" or sep == "\n\n" else c + "")
        # For newline separators we prepended; normalise by re-splitting cleanly.
        return [p for p in (text.split(sep)) if p] if sep.startswith("\n") else out

    def _hard_char_split(self, text: str) -> List[str]:
        """Absolute fallback: slice by character budget derived from chunk_size."""
        max_chars = max(1, int(self.chunk_size * self._chars_per_token_estimate()))
        return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

    def _chars_per_token_estimate(self) -> float:
        # Invert the length function on a probe string to estimate chars/token.
        probe = "x" * 100
        toks = max(1, self._len(probe))
        return 100 / toks

    # ── Windowing with overlap ────────────────────────────────────────────────
    #
    # Budget is enforced on the *character length of the joined window* rather
    # than a sum of per-fragment token counts. Per-fragment int() flooring
    # underestimates the joined total (each floor drops up to ~1 token, and N
    # fragments compound that error), which is how a "512" window can measure
    # 546 downstream. Accounting in chars — the exact thing _join produces and
    # _len consumes — removes that drift.

    def _merge_with_overlap(self, splits: List[str]) -> List[str]:
        """
        Greedily pack fragments into windows up to chunk_size tokens, then seed
        the next window with a trailing slice worth ~chunk_overlap tokens so
        adjacent chunks share context.
        """
        cpt          = self._chars_per_token_estimate()
        budget_chars = int(self.chunk_size * cpt)
        ovl_chars    = int(self.chunk_overlap * cpt)

        chunks: List[str] = []
        current: List[str] = []      # fragment strings (already stripped)
        current_chars = 0            # running length of the joined window

        def window_len_after(add_len: int) -> int:
            # +1 for the single space _join inserts, when the window is non-empty
            return current_chars + (1 if current else 0) + add_len

        def flush() -> None:
            nonlocal current, current_chars
            if not current:
                return
            chunks.append(" ".join(current).strip())
            if ovl_chars > 0:
                tail = self._char_tail(current, ovl_chars)
                current = tail
                current_chars = len(" ".join(current))
            else:
                current, current_chars = [], 0

        for raw in splits:
            frag = raw.strip()
            if not frag:
                continue
            flen = len(frag)

            # Fragment alone exceeds budget (shouldn't survive recursion, but
            # guard): flush what we have and emit it standalone.
            if flen > budget_chars:
                flush()
                if current:
                    chunks.append(" ".join(current).strip())
                    current, current_chars = [], 0
                chunks.append(frag)
                continue

            if window_len_after(flen) > budget_chars and current:
                flush()
            # After flush, current may hold the overlap tail; append frag to it.
            current.append(frag)
            current_chars = len(" ".join(current))

        if current:
            chunks.append(" ".join(current).strip())

        # Drop windows that are pure duplicates of their predecessor (can happen
        # when a lone over-budget fragment is flanked by its overlap tail).
        deduped: List[str] = []
        for c in chunks:
            c = c.strip()
            if c and (not deduped or c != deduped[-1]):
                deduped.append(c)
        return deduped

    @staticmethod
    def _char_tail(frags: List[str], overlap_chars: int) -> List[str]:
        """
        Trailing fragments whose joined length is ≈ overlap_chars (≤, if possible).

        After collecting fragments, any leading fragment that is a *complete*
        sentence (ends with terminal punctuation) is dropped from the head of
        the tail.  Such fragments belong entirely to the flushed chunk and
        would make the next chunk appear to start mid-document (e.g. the next
        chunk would open with "deployment. These views…" where "deployment."
        is the dangling tail of the previous section's last sentence).
        """
        tail: List[str] = []
        total = 0
        for frag in reversed(frags):
            add = len(frag) + (1 if tail else 0)
            if total + add > overlap_chars and tail:
                break
            tail.insert(0, frag)
            total += add

        # Drop leading fragments that are complete sentences so the seeded
        # overlap never starts a new chunk with a sentence-final fragment.
        while len(tail) > 1 and _TERMINAL_PUNCT.search(tail[0]):
            tail.pop(0)

        return tail

    @staticmethod
    def _join(frags: List[str]) -> str:
        return " ".join(f.strip() for f in frags if f.strip()).strip()


# ── Token-correct windowed chunk splitter ────────────────────────────────────
# This is the corrected version of the chunk-splitting logic described in the
# KnowledgeBuilder design doc.
#
# THE BUG IN THE REFERENCE CODE (now fixed here):
#   The reference _split_text_into_chunks computed the threshold via token
#   count (tokenizer.encode → int) but then sliced by CHARACTER index in the
#   loop body.  For English text at ~4 chars/token this overshoots the context
#   window by ~4x, sending chunks far larger than intended to the LLM.
#
# THE FIX:
#   Encode the full text to a token list once; slice the TOKEN list per
#   window; decode each slice back to text.  Both the threshold check and the
#   loop body now operate in the same unit (tokens), so chunk sizes are exact.
#
# Usage:
#     from src.services.ingestion.chunkers.splitter import split_text_into_token_windows
#
#     chunks = split_text_into_token_windows(
#         text=content,
#         tokenizer=model_config.tokenizer,
#         context_window=4096,
#         overlap_fraction=0.05,   # 5 % overlap  (matches the reference spec)
#     )

def split_text_into_token_windows(
    text: str,
    tokenizer,                  # any object with .encode(text, add_special_tokens) → list[int]
                                # and .decode(ids) → str
    context_window: int,
    overlap_fraction: float = 0.05,
) -> list[str]:
    """Split *text* into token-exact windows of at most *context_window* tokens.

    Implements the chunking contract from the KnowledgeBuilder flow diagram:
        Document markdown
          → split_text_into_token_windows  (5 % overlap by default)
          → [Chunk 1, Chunk 2, ... Chunk n]
          → _execute_parallel_requests   (asyncio.gather in batches)
          → merge pass
          → RAW_KNOWLEDGE.md

    Parameters
    ----------
    text             : raw document text (after strip_non_ascii / cleaning)
    tokenizer        : HuggingFace-compatible tokenizer
    context_window   : maximum tokens per window (hard ceiling)
    overlap_fraction : fraction of context_window to overlap between consecutive
                       windows (default 0.05 = 5 %, matching the reference spec)

    Returns
    -------
    List of decoded text strings, each fitting within *context_window* tokens.
    If the full text already fits, a single-element list is returned.

    Bug fixed vs reference _split_text_into_chunks
    -----------------------------------------------
    The original code computed the threshold in TOKENS but then sliced by
    CHARACTER index — overshooting the context window by ~4x for English text.
    This implementation encodes once, slices the TOKEN list per window, then
    decodes each slice back — both gate and loop body operate in the same unit.
    """
    tokens: list[int] = tokenizer.encode(text, add_special_tokens=False)

    # Fast path: text already fits in one window — no chunking needed.
    if len(tokens) <= context_window:
        return [text]

    overlap: int = max(0, int(context_window * overlap_fraction))
    step: int = context_window - overlap  # tokens advanced per window

    chunks: list[str] = []
    start = 0
    while start < len(tokens):
        end = min(start + context_window, len(tokens))
        chunk_tokens = tokens[start:end]
        chunks.append(tokenizer.decode(chunk_tokens))
        if end == len(tokens):
            break
        start += step  # slide forward by (context_window - overlap)

    return chunks
