"""
Structured logging setup.

Usage
─────
    from src.utils.logging import get_logger
    logger = get_logger(__name__)
"""
from __future__ import annotations

import logging
import sys
from functools import lru_cache


_FMT  = "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s"
_DATEFMT = "%Y-%m-%dT%H:%M:%S"


# Third-party loggers that produce noisy INFO lines we don't want.
_QUIET_LOGGERS = [
    "httpx",
    "httpcore",
    "urllib3",
    "pymilvus",
]


def _setup_root_logger(level: str = "INFO") -> None:
    root = logging.getLogger()
    if root.handlers:
        return  # already configured

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(_FMT, datefmt=_DATEFMT))
    root.addHandler(handler)
    root.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Suppress noisy third-party INFO / DEBUG logs
    for name in _QUIET_LOGGERS:
        logging.getLogger(name).setLevel(logging.WARNING)


@lru_cache(maxsize=None)
def get_logger(name: str) -> logging.Logger:
    """Return a module-level logger.  Safe to call at import time."""
    # Defer settings import to avoid circular imports at module load
    try:
        from src.config.settings import get_settings
        level = get_settings().log_level
    except Exception:
        level = "INFO"

    _setup_root_logger(level)
    return logging.getLogger(name)
