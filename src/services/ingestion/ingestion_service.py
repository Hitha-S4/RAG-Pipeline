"""
IngestionService — thin async wrapper around EntityPipeline.

EntityPipeline.run() is synchronous (blocking LLM + embedding calls).
IngestionService wraps it in asyncio.to_thread so the FastAPI event loop
is never blocked, and returns a PipelineContext whose fields match
IngestResponse.
"""
from __future__ import annotations

import asyncio
import traceback
from datetime import datetime, timezone

from src.enums import IngestionStatus, SourceType
from src.models.pipeline_context import PipelineContext
from src.services.ingestion.entity_pipeline import EntityPipeline
from src.utils.logging import get_logger

logger = get_logger(__name__)


class IngestionService:
    """Async facade over the synchronous EntityPipeline."""

    def __init__(self) -> None:
        self._pipeline = EntityPipeline()

    async def ingest(
        self,
        source: str,
        source_type: SourceType,
    ) -> PipelineContext:
        """
        Run the full ingestion pipeline for *source*.

        Returns a PipelineContext — always returns, never raises.
        Check ``.status`` / ``.error`` on the returned context.
        """
        ctx = PipelineContext(source=source, source_type=source_type)

        try:
            result: dict = await asyncio.to_thread(
                self._pipeline.run, source, source_type
            )
            ctx.status      = IngestionStatus.COMPLETED
            ctx.chunk_count = result.get("chunks", 0)
            ctx.doc_id      = source
        except Exception as exc:
            ctx.status = IngestionStatus.FAILED
            ctx.error  = str(exc)
            logger.error(
                "Pipeline failed  source=%s  error=%s\n%s",
                source, exc, traceback.format_exc(),
            )
        finally:
            ctx.finished_at = datetime.now(timezone.utc)

        return ctx
