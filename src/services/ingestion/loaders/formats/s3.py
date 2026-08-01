"""S3 loader — downloads an S3 object and delegates to the right type loader."""
from __future__ import annotations

import io
from pathlib import Path

from src.enums import SourceType
from src.models import Document, DocumentMetadata
from src.utils.logging import get_logger

from .base import BaseLoader

logger = get_logger(__name__)


class S3Loader(BaseLoader):
    """
    Downloads an object from S3 into memory and delegates to the appropriate
    type-specific loader based on the object key's file extension.

    Source URI format: ``s3://bucket/key``
    """

    def get_supported_extensions(self) -> list[str]:
        return [".pdf", ".txt", ".md", ".mdx", ".html", ".htm", ".csv", ".json"]

    def load(self, source: str, **kwargs) -> Document:
        try:
            import boto3  # type: ignore
        except ImportError:
            raise RuntimeError("boto3 is required: pip install boto3")

        assert source.startswith("s3://"), "S3 source must start with s3://"
        _, _, rest = source.partition("s3://")
        bucket, _, key = rest.partition("/")

        s3 = boto3.client("s3")
        obj = s3.get_object(Bucket=bucket, Key=key)
        body_bytes: bytes = obj["Body"].read()

        suffix = Path(key).suffix.lower()

        if suffix == ".pdf":
            try:
                import pdfplumber  # type: ignore
            except ImportError:
                raise RuntimeError("pdfplumber is required: pip install pdfplumber")
            import tempfile, os
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp.write(body_bytes)
                tmp_path = tmp.name
            try:
                from src.services.ingestion.loaders.formats.pdf import _extract_with_pdfplumber
                from pathlib import Path as _Path
                content = _extract_with_pdfplumber(_Path(tmp_path))
            finally:
                os.unlink(tmp_path)
            with pdfplumber.open(io.BytesIO(body_bytes)) as pdf:
                n_pages = len(pdf.pages)
            logger.info("S3 PDF loaded: %s  pages=%d", key, n_pages)
            return Document(
                content=content,
                metadata=DocumentMetadata(
                    source_name=Path(key).stem,
                    source_type=SourceType.PDF,
                    original_filename=key,
                    url=source,
                ),
            )

        # All other extensions treated as plain text
        content = body_bytes.decode("utf-8", errors="replace")
        logger.info("S3 text loaded: %s  chars=%d", key, len(content))
        return Document(
            content=content,
            metadata=DocumentMetadata(
                source_name=Path(key).stem,
                source_type=SourceType.TEXT,
                original_filename=key,
                url=source,
            ),
        )
