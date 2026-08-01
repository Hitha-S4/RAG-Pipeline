"""
Milvus vector store service.

Supports Milvus Lite (embedded) and Milvus Standalone (remote).
Mode is controlled by MILVUS_MODE env var.

Collection schema (all stored per leaf chunk)
──────────────────────────────────────────────
    chunk_id          VARCHAR(64)    primary key
    chunk_type        VARCHAR(32)
    sub_type          VARCHAR(32)    lifecycle action (install/configure/...)
    depth             INT
    is_leaf           BOOL
    parent_id         VARCHAR(64)
    children_ids      VARCHAR(2048)  JSON-encoded list[str]
    content_hash      VARCHAR(64)
    headings          VARCHAR(1024)  JSON-encoded list[str]
    content           VARCHAR(65535)
    summary           VARCHAR(8192)
    questions         VARCHAR(4096)  JSON-encoded list[str] (hypothetical questions)
    embedding         FLOAT_VECTOR(dimension)
    summary_embedding FLOAT_VECTOR(dimension)
"""
from __future__ import annotations

import json
from typing import Any, Optional

from src.config.settings import get_settings
from src.models import Chunk
from src.models.query import RetrievedChunk
from src.utils.logging import get_logger

logger = get_logger(__name__)

_MAX_VARCHAR = 65_535


def _truncate(value: str, max_len: int = _MAX_VARCHAR) -> str:
    return value[:max_len] if len(value) > max_len else value


def _enum_value(value) -> str:
    """Return the .value of a str-Enum member, or str(value) for plain strings.

    Guards against ``str(ChunkCategory.WORKFLOWS)`` producing the repr
    ``'ChunkCategory.WORKFLOWS'`` instead of the stored value ``'workflows'``.
    """
    return getattr(value, "value", value) if value is not None else ""


class MilvusService:
    """
    Thin pymilvus wrapper.
      • Auto-creates collection with full N-level tree schema on first use.
      • Batched upsert to stay under the 64 MB gRPC limit.
      • ANN search with optional metadata filters.
      • DFS helpers: fetch_subtree, fetch_ancestors.
    """

    _UPSERT_BATCH_ROWS = 200

    def __init__(self):
        self._settings  = get_settings()
        self._client    = None   # type: ignore[assignment]
        self._connected = False

    # ── Connection ────────────────────────────────────────────────────────────

    @staticmethod
    def _ensure_docker_running(host: str, port: int) -> None:
        """If the Milvus standalone port is unreachable, attempt to start the
        ``milvus-standalone`` Docker container and wait up to 30 s for it to
        become healthy.  No-ops when Docker is unavailable or when the port is
        already reachable (i.e. non-Docker deployments are unaffected).

        Root cause this guards against: the milvus-standalone container exits
        with "etcdserver: requested lease not found" after an etcd lease expiry
        (observed when the etcd container restarts while milvus is running).
        The fix for users is ``docker start milvus-standalone``; this method
        does it automatically so the ingestion pipeline self-heals.
        """
        import socket, subprocess, time

        # Fast path: port is already open → nothing to do.
        try:
            with socket.create_connection((host, port), timeout=2):
                return
        except OSError:
            pass

        logger.warning(
            "Milvus port %s:%d unreachable — attempting to start milvus-standalone container",
            host, port,
        )

        # Try docker start; ignore errors if Docker is absent.
        try:
            result = subprocess.run(
                ["docker", "start", "milvus-standalone"],
                capture_output=True, text=True, timeout=15,
            )
            if result.returncode != 0:
                logger.warning(
                    "docker start milvus-standalone failed (rc=%d): %s",
                    result.returncode, result.stderr.strip(),
                )
                return
            logger.info("docker start milvus-standalone → OK, waiting for port %d …", port)
        except Exception as exc:
            logger.warning("Could not run docker start: %s", exc)
            return

        # Wait up to 30 s for the port to open.
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            time.sleep(2)
            try:
                with socket.create_connection((host, port), timeout=2):
                    logger.info("Milvus port %s:%d is now reachable", host, port)
                    return
            except OSError:
                pass

        logger.error(
            "Milvus port %s:%d still unreachable after 30 s — connection will likely fail",
            host, port,
        )

    def _connect(self):
        if self._connected:
            return
        try:
            from pymilvus import MilvusClient  # type: ignore
        except ImportError:
            raise RuntimeError("pymilvus is required: pip install pymilvus")

        s = self._settings
        if s.milvus_mode == "lite":
            import os
            os.makedirs(os.path.dirname(s.milvus_lite_path) or ".", exist_ok=True)
            self._client = MilvusClient(s.milvus_lite_path)
            logger.info("Milvus Lite connected: %s", s.milvus_lite_path)
        else:
            # Auto-heal: start the Docker container if the port is down.
            self._ensure_docker_running(s.milvus_host, s.milvus_port)
            uri = f"http://{s.milvus_host}:{s.milvus_port}"
            self._client = MilvusClient(
                uri=uri,
                user=s.milvus_user or None,
                password=s.milvus_password or None,
            )
            logger.info("Milvus Standalone connected: %s", uri)

        self._ensure_collection()
        self._connected = True

    def _ensure_collection(self, recreate: bool = False):
        from pymilvus import DataType  # type: ignore
        s    = self._settings
        name = s.milvus_collection

        if self._client.has_collection(name):
            if not recreate:
                logger.debug("Collection '%s' already exists", name)
                return
            logger.warning("Collection '%s' exists but storage is corrupt — dropping and recreating", name)
            self._client.drop_collection(name)

        schema = self._client.create_schema(auto_id=False, enable_dynamic_field=False)
        schema.add_field("chunk_id",      DataType.VARCHAR,      max_length=64,          is_primary=True)
        schema.add_field("chunk_type",    DataType.VARCHAR,      max_length=32)
        schema.add_field("sub_type",      DataType.VARCHAR,      max_length=32)
        schema.add_field("depth",         DataType.INT32)
        schema.add_field("is_leaf",       DataType.BOOL)
        schema.add_field("parent_id",     DataType.VARCHAR,      max_length=64)
        schema.add_field("children_ids",  DataType.VARCHAR,      max_length=2048)
        schema.add_field("content_hash",  DataType.VARCHAR,      max_length=64)
        schema.add_field("headings",      DataType.VARCHAR,      max_length=1024)
        schema.add_field("content",           DataType.VARCHAR,      max_length=_MAX_VARCHAR)
        schema.add_field("summary",           DataType.VARCHAR,      max_length=8192)
        schema.add_field("questions",         DataType.VARCHAR,      max_length=4096,
                         nullable=True, default_value="[]")
        schema.add_field("embedding",         DataType.FLOAT_VECTOR, dim=s.milvus_dimension)
        schema.add_field("summary_embedding", DataType.FLOAT_VECTOR, dim=s.milvus_dimension)

        idx = self._client.prepare_index_params()
        idx.add_index(
            field_name="embedding",
            index_type="HNSW",
            metric_type="COSINE",
            params={"M": 16, "efConstruction": 200},
        )
        idx.add_index(
            field_name="summary_embedding",
            index_type="HNSW",
            metric_type="COSINE",
            params={"M": 16, "efConstruction": 200},
        )
        self._client.create_collection(
            collection_name=name,
            schema=schema,
            index_params=idx,
        )
        logger.info("Collection '%s' created  dim=%d", name, s.milvus_dimension)

    # ── Write ─────────────────────────────────────────────────────────────────

    async def upsert_chunks(self, chunks: list[Chunk]) -> int:
        """
        Upsert leaf chunks in batches of _UPSERT_BATCH_ROWS to stay under
        the 64 MB gRPC message limit. Returns total rows upserted.
        """
        self._connect()
        if not chunks:
            return 0

        rows: list[dict[str, Any]] = []
        for c in chunks:
            if not c.embedding:
                logger.warning("Chunk %s has no embedding — skipping", c.chunk_id)
                continue
            rows.append({
                "chunk_id":      c.chunk_id[:64],
                "chunk_type":    _truncate(_enum_value(c.metadata.chunk_type), 32),
                "sub_type":      _truncate(_enum_value(c.metadata.sub_type) or "other", 32),
                "depth":         c.metadata.depth,
                "is_leaf":       c.metadata.is_leaf,
                "parent_id":     _truncate(c.metadata.parent_id or "", 64),
                "children_ids":  _truncate(json.dumps(c.metadata.children_ids), 2048),
                "content_hash":  _truncate(c.content_hash, 64),
                "headings":      _truncate(json.dumps(c.metadata.headings), 1024),
                "content":           _truncate(c.content),
                "summary":           _truncate(c.summary, 8192),
                "questions":         _truncate(json.dumps(getattr(c, "questions", [])), 4096),
                "embedding":         c.embedding,
                "summary_embedding": c.summary_embedding,
            })

        total = 0
        for i in range(0, len(rows), self._UPSERT_BATCH_ROWS):
            batch = rows[i: i + self._UPSERT_BATCH_ROWS]
            try:
                self._client.upsert(collection_name=self._settings.milvus_collection, data=batch)
            except Exception as exc:
                if "collection not found" in str(exc).lower():
                    logger.warning("Collection missing during upsert — recreating and retrying: %s", exc)
                    self._ensure_collection(recreate=True)
                    self._client.upsert(collection_name=self._settings.milvus_collection, data=batch)
                else:
                    raise
            total += len(batch)
            logger.info(
                "Upserted batch %d-%d / %d into '%s'",
                i + 1, i + len(batch), len(rows), self._settings.milvus_collection,
            )
        return total

    # ── Read ──────────────────────────────────────────────────────────────────

    _OUTPUT_FIELDS = [
        "chunk_id", "chunk_type", "sub_type",
        "depth", "is_leaf", "parent_id", "children_ids",
        "content_hash", "headings", "content", "summary",
    ]

    @staticmethod
    def _safe_json_list(raw: str) -> list:
        """Parse a JSON list field; return [] on any parse error (e.g. truncation)."""
        if not raw:
            return []
        try:
            return json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            return []

    def _entity_to_retrieved(self, entity: dict, score: float = 0.0) -> RetrievedChunk:
        return RetrievedChunk(
            chunk_id=entity.get("chunk_id", ""),
            content=entity.get("content", ""),
            summary=entity.get("summary", ""),
            score=score,
            depth=entity.get("depth", 0),
            is_leaf=entity.get("is_leaf", True),
            parent_id=entity.get("parent_id") or None,
            children_ids=self._safe_json_list(entity.get("children_ids", "[]")),
            metadata={
                "chunk_type":   entity.get("chunk_type", ""),
                "sub_type":     entity.get("sub_type", ""),
                "content_hash": entity.get("content_hash", ""),
                "headings":     self._safe_json_list(entity.get("headings", "[]")),
            },
        )

    async def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
        filter_expr: str = "",
        score_threshold: float = 0.0,
        anns_field: str | None = None,
    ) -> list[RetrievedChunk]:
        """
        ANN search — returns leaf chunks sorted by descending score.

        The vector field searched is chosen by *anns_field*, defaulting from
        ``settings.search_on_summary``:
          • True  → ``summary_embedding``  (brief abstractive gist — default)
          • False → ``embedding``          (raw content vector)

        The query vector must have been produced by the SAME embedding model
        used for the target field (the caller's ``embed_query`` handles this).
        """
        self._connect()

        field = anns_field or (
            "summary_embedding" if getattr(self._settings, "search_on_summary", True)
            else "embedding"
        )

        results = self._client.search(
            collection_name=self._settings.milvus_collection,
            data=[query_vector],
            anns_field=field,
            search_params={"metric_type": "COSINE", "params": {"ef": 64}},
            limit=top_k,
            filter=filter_expr or None,
            output_fields=self._OUTPUT_FIELDS,
        )

        retrieved: list[RetrievedChunk] = []
        for hit in results[0]:
            score = hit.get("distance", 0.0)
            if score < score_threshold:
                continue
            entity = hit.get("entity", {})
            chunk  = self._entity_to_retrieved(entity, score)
            logger.debug(
                "cosine  field=%-20s  score=%.4f  chunk=%.8s  type=%-12s  headings=%s",
                field,
                score,
                chunk.chunk_id,
                entity.get("chunk_type", "?"),
                self._safe_json_list(entity.get("headings", "[]")),
            )
            retrieved.append(chunk)

        if retrieved:
            scores = [c.score for c in retrieved]
            logger.info(
                "search  field=%-20s  hits=%d  top=%.4f  mean=%.4f  min=%.4f  filter=%r",
                field,
                len(retrieved),
                scores[0],
                sum(scores) / len(scores),
                scores[-1],
                filter_expr or "",
            )
        else:
            logger.info(
                "search  field=%-20s  hits=0  filter=%r",
                field, filter_expr or "",
            )

        return retrieved

    async def fetch_by_ids(self, chunk_ids: list[str]) -> list[RetrievedChunk]:
        """Fetch specific chunks by primary key — used by graph traversal."""
        if not chunk_ids:
            return []
        self._connect()
        results = self._client.get(
            collection_name=self._settings.milvus_collection,
            ids=chunk_ids,
            output_fields=self._OUTPUT_FIELDS,
        )
        return [self._entity_to_retrieved(e) for e in results]

    async def fetch_ancestors(self, chunk_id: str) -> list[RetrievedChunk]:
        """Walk parent_id chain from chunk_id up to the root (shallowest first)."""
        chain: list[RetrievedChunk] = []
        seen: set[str] = set()
        current: str | None = chunk_id
        while current and current not in seen:
            seen.add(current)
            fetched = await self.fetch_by_ids([current])
            if not fetched:
                break
            node = fetched[0]
            chain.append(node)
            current = node.parent_id
        chain.reverse()
        return chain[:-1]   # exclude the node itself (root first)

    async def fetch_subtree(self, root_id: str, max_nodes: int = 128) -> list[RetrievedChunk]:
        """DFS downward from root_id — returns nodes in document order."""
        visited: set[str] = set()
        ordered: list[RetrievedChunk] = []
        stack = [root_id]
        while stack and len(ordered) < max_nodes:
            cid = stack.pop()
            if cid in visited:
                continue
            visited.add(cid)
            fetched = await self.fetch_by_ids([cid])
            if not fetched:
                continue
            node = fetched[0]
            ordered.append(node)
            for child_id in reversed(node.children_ids):
                if child_id not in visited:
                    stack.append(child_id)
        return ordered

    # ── Delete / maintenance ──────────────────────────────────────────────────

    async def delete_by_doc_id(self, doc_id: str) -> int:
        """Hard delete all chunks for a document."""
        self._connect()
        result = self._client.delete(
            collection_name=self._settings.milvus_collection,
            filter=f'doc_id == "{doc_id}"',
        )
        count = result.get("delete_count", 0)
        logger.info("Hard-deleted %d chunks for doc_id=%s", count, doc_id)
        return count

    async def drop_collection(self) -> dict[str, Any]:
        """Drop the entire collection. Recreated automatically on next use."""
        self._connect()
        name = self._settings.milvus_collection
        self._client.drop_collection(name)
        self._connected = False
        self._client    = None
        logger.info("Collection '%s' dropped", name)
        return {"dropped": name}

    async def get_collection_stats(self) -> dict[str, Any]:
        self._connect()
        return dict(self._client.get_collection_stats(self._settings.milvus_collection))
