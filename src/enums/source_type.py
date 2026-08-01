from enum import Enum


class SourceType(str, Enum):
    """Supported ingestion source types."""
    PDF       = "pdf"
    TEXT      = "text"
    MARKDOWN  = "markdown"
    HTML      = "html"
    CSV       = "csv"
    JSON      = "json"
    URL       = "url"   # HTML source fetched from a web URL (handled by HTMLLoader)
