"""
Content cleaners — generic, format-agnostic text transforms applied AFTER a
loader extracts raw text but BEFORE chunking.

Each cleaner is a pure function ``(text: str, ...) -> str`` with no dependency on
the source format, so the same cleaner can run for PDF, HTML, or Markdown.
"""
from .command_reference import (
    CommandReferenceStats,
    analyze_command_reference,
    strip_command_reference,
)
from .text_cleaner import non_ascii_ratio, to_ascii

__all__ = [
    "strip_command_reference",
    "analyze_command_reference",
    "CommandReferenceStats",
    "to_ascii",
    "non_ascii_ratio",
]
