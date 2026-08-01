"""Loader formats — concrete BaseLoader implementations."""
from __future__ import annotations

from .base import BaseLoader, LoaderProtocol
from .csv import CSVLoader
from .html import HTMLLoader
from .json_loader import JSONLoader
from .pdf import PDFLoader
from .s3 import S3Loader
from .text import TextLoader

__all__ = [
    "BaseLoader",
    "LoaderProtocol",
    "CSVLoader",
    "HTMLLoader",
    "JSONLoader",
    "PDFLoader",
    "S3Loader",
    "TextLoader",
]
