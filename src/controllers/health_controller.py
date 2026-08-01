"""Health check controller."""
from datetime import datetime, timezone

from fastapi import APIRouter

from src.config.settings import get_settings
from src.services.vectordb.milvus_service import MilvusService
from src.utils.logging import get_logger

router = APIRouter(prefix="/health", tags=["Health"])   # mounted at /api/v1/health
logger = get_logger(__name__)

_milvus = MilvusService()


@router.get("", summary="Liveness probe")
async def health():
    """Returns 200 if the API process is running."""
    s = get_settings()
    return {
        "status": "ok",
        "app":    s.app_name,
        "env":    s.app_env,
        "time":   datetime.now(timezone.utc).isoformat(),
    }


@router.get("/ready", summary="Readiness probe — checks Milvus connectivity")
async def readiness():
    """Returns 200 when Milvus is reachable and the collection exists."""
    try:
        stats = await _milvus.get_collection_stats()
        return {"status": "ready", "milvus": stats}
    except Exception as exc:
        logger.warning("Readiness check failed: %s", exc)
        from fastapi import HTTPException
        raise HTTPException(status_code=503, detail=f"Milvus unavailable: {exc}")
