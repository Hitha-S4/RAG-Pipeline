from enum import Enum


class ChunkCategory(str, Enum):
    """Semantic category assigned to each chunk during classification."""
    FEATURES    = "features"
    WORKFLOWS   = "workflows"
    PERSONAS    = "personas"
    KNOWLEDGE   = "knowledge"
    KEYWORDS    = "keywords"
    ENTITIES    = "entities"
