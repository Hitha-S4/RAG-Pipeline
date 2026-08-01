from enum import Enum


class ChunkSubType(str, Enum):
    """
    Lifecycle / action sub-type assigned to each chunk during classification.

    This is the second classification axis (orthogonal to ChunkCategory).
    It answers *"which lifecycle action is this content about?"* and drives
    action-scoped retrieval — e.g. "how to configure X" fetches the
    ``configure`` slice across personas, features, and workflows.

    Values are intentionally generic (data-source independent): they describe
    documentation lifecycle stages, not any specific product.
    """
    INSTALL      = "install"
    UNINSTALL    = "uninstall"
    UPGRADE      = "upgrade"
    CONFIGURE    = "configure"
    INTEGRATE    = "integrate"
    ADMINISTER   = "administer"
    MONITOR      = "monitor"
    TROUBLESHOOT = "troubleshoot"
    USAGE        = "use"
    REFERENCE    = "reference"
    OVERVIEW     = "overview"
    OTHER        = "other"
