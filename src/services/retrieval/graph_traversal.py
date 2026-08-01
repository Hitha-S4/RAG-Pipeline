"""
Chunk graph traversal — Depth-First (DFS) and Breadth-First (BFS) over the
N-level chunk tree stored in Milvus.

DFS → go DEEP. From a seed, dive down one branch fully before the next.
      Produces nodes in document order → ideal for reconstructing an ordered
      procedure (a Workflow's Step 1 → 2 → 3 …).

BFS → go WIDE. Expand level-by-level from a seed (or a whole frontier).
      Produces the immediate neighbourhood first → ideal for gathering breadth
      of related context (siblings, same-depth sections, the parent that ties
      them together).

Traversal is bounded by max_nodes / max_depth to prevent runaway queries.
"""
from __future__ import annotations

from collections import deque
from typing import Any, Iterable, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.query import RetrievedChunk


class _NodeReader(Protocol):
    async def fetch_by_ids(self, chunk_ids: list[str]) -> list[Any]: ...


def _dedupe_preserve(ids: Iterable[str]) -> list[str]:
    """Order-preserving de-duplication."""
    return list(dict.fromkeys(i for i in ids if i))


class ChunkGraphTraversal:
    """
    Stateless traversal helper bound to a vector-store reader.

        traversal = ChunkGraphTraversal(milvus_service)
        subtree   = await traversal.dfs("chunk-abc")          # deep, ordered
        level     = await traversal.bfs("chunk-abc")          # wide, by level
        around    = await traversal.bfs_neighborhood(seeds)   # related context
        path      = await traversal.ancestors("chunk-abc")    # heading breadcrumb
    """

    def __init__(self, vectordb: "_NodeReader"):
        self._vdb = vectordb

    # ── DFS (deep, ordered) ───────────────────────────────────────────────────

    async def dfs(self, root_id: str, max_nodes: int = 128) -> list["RetrievedChunk"]:
        """
        Iterative pre-order DFS downward through children_ids.
        Returns nodes in depth-first document order (left-most child first).
        """
        visited: set[str] = set()
        ordered: list[Any] = []
        stack: list[str] = [root_id]

        while stack and len(ordered) < max_nodes:
            cid = stack.pop()
            if cid in visited:
                continue
            visited.add(cid)
            fetched = await self._vdb.fetch_by_ids([cid])
            if not fetched:
                continue
            node = fetched[0]
            ordered.append(node)
            for child_id in reversed(node.children_ids):
                if child_id not in visited:
                    stack.append(child_id)

        return ordered

    # ── BFS (wide, level-order) ───────────────────────────────────────────────

    async def bfs(
        self,
        root_id: str,
        max_depth: int = 3,
        max_nodes: int = 128,
    ) -> list["RetrievedChunk"]:
        """
        Level-order BFS downward through children_ids.
        Fetches an entire frontier in a single fetch_by_ids call per level.
        """
        ordered: list[Any] = []
        visited: set[str] = {root_id}
        frontier: list[str] = [root_id]
        depth = 0

        while frontier and depth <= max_depth and len(ordered) < max_nodes:
            level_nodes = await self._vdb.fetch_by_ids(frontier)
            by_id = {n.chunk_id: n for n in level_nodes}
            next_frontier: list[str] = []

            for cid in frontier:
                node = by_id.get(cid)
                if node is None:
                    continue
                ordered.append(node)
                if len(ordered) >= max_nodes:
                    break
                for child_id in node.children_ids:
                    if child_id not in visited:
                        visited.add(child_id)
                        next_frontier.append(child_id)

            frontier = next_frontier
            depth += 1

        return ordered[:max_nodes]

    # ── BFS neighbourhood (undirected, multi-seed) ────────────────────────────

    async def bfs_neighborhood(
        self,
        seed_ids: list[str],
        hops: int = 1,
        max_nodes: int = 64,
    ) -> list["RetrievedChunk"]:
        """
        Undirected BFS from a set of ANN seed nodes.
        Each node's neighbours = children_ids + parent_id.
        Used for breadth-of-related-context (keywords / personas / features).
        """
        seen: set[str] = set()
        ordered: list[Any] = []
        frontier = _dedupe_preserve(seed_ids)
        seen.update(frontier)
        hop = 0

        while frontier and hop <= hops and len(ordered) < max_nodes:
            nodes = await self._vdb.fetch_by_ids(frontier)
            by_id = {n.chunk_id: n for n in nodes}
            next_frontier: list[str] = []

            for cid in frontier:
                node = by_id.get(cid)
                if node is None:
                    continue
                ordered.append(node)
                if len(ordered) >= max_nodes:
                    break
                neighbours = list(node.children_ids)
                if node.parent_id:
                    neighbours.append(node.parent_id)
                for nb in neighbours:
                    if nb not in seen:
                        seen.add(nb)
                        next_frontier.append(nb)

            frontier = next_frontier
            hop += 1

        return ordered[:max_nodes]

    # ── Upward path (heading breadcrumb) ──────────────────────────────────────

    async def ancestors(self, chunk_id: str, max_depth: int = 16) -> list["RetrievedChunk"]:
        """
        Walk parent_id chain up to the root.
        Returns [root, …, direct_parent] (shallowest first), excluding the node itself.
        """
        chain: list[Any] = []
        seen: set[str] = set()
        current: str | None = chunk_id
        steps = 0

        while current and current not in seen and steps < max_depth:
            seen.add(current)
            fetched = await self._vdb.fetch_by_ids([current])
            if not fetched:
                break
            node = fetched[0]
            chain.append(node)
            current = node.parent_id
            steps += 1

        chain.reverse()       # root first
        return chain[:-1]     # drop the node itself
