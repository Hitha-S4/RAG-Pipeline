from enum import Enum


class IngestionStatus(str, Enum):
    """Lifecycle states of an ingestion job."""
    PENDING    = "pending"
    LOADING    = "loading"
    PROCESSING = "processing"
    CHUNKING   = "chunking"
    EMBEDDING  = "embedding"
    STORING    = "storing"
    COMPLETED  = "completed"
    FAILED     = "failed"
