# genai-rag-pipeline — Architecture & Developer Reference

> **Version:** 1.1.0 · **Stack:** Python 3.11+, FastAPI, Milvus, an LLM provider, sentence-transformers
>
> A production-oriented RAG (**Retrieval-Augmented Generation**) ingestion and retrieval backend for technical documentation. The service ingests multi-format documents, classifies and embeds every chunk, persists them in a vector store, and exposes two query modes: a simple ANN search and a full agentic retrieval flow.

---

## Table of Contents

1. [Project Layout](#1-project-layout)
2. [Configuration & Environment](#2-configuration--environment)
3. [Application Entry Point](#3-application-entry-point)
4. [API Surface](#4-api-surface)
5. [Data Model](#5-data-model)
6. [Ingestion Pipeline](#6-ingestion-pipeline)
   - 6.1 [Document Loaders](#61-document-loaders)
   - 6.2 [Text Cleaning](#62-text-cleaning)
   - 6.3 [LLM Service & Windowing](#63-llm-service--windowing)
   - 6.4 [Entity Extraction (EntityPipeline)](#64-entity-extraction-entitypipeline)
   - 6.5 [Chunking Strategies](#65-chunking-strategies)
   - 6.6 [Classification & Summarization](#66-classification--summarization)
   - 6.7 [Embedding Service](#67-embedding-service)
   - 6.8 [Output Writers](#68-output-writers)
7. [Vector Store (Milvus)](#7-vector-store-milvus)
8. [Retrieval — Basic Path](#8-retrieval--basic-path)
9. [Retrieval — Agentic Path](#9-retrieval--agentic-path)
   - 9.1 [Step 1: Query Rewrite & Multi-Query Expansion](#91-step-1-query-rewrite--multi-query-expansion)
   - 9.2 [Step 2: Facet Extraction](#92-step-2-facet-extraction)
   - 9.3 [Step 3: Facet Detail Fetch (RRF)](#93-step-3-facet-detail-fetch-rrf)
   - 9.4 [Step 4: Intent & Sub-type Detection](#94-step-4-intent--sub-type-detection)
   - 9.5 [Step 5a: Informational Branch](#95-step-5a-informational-branch)
   - 9.6 [Step 5b: Action Branch](#96-step-5b-action-branch)
10. [Scoring & Ranking](#10-scoring--ranking)
    - 10.1 [Composite Score](#101-composite-score)
    - 10.2 [Rank Score](#102-rank-score)
    - 10.3 [Topic Centrality](#103-topic-centrality)
    - 10.4 [Sub-type Agreement](#104-sub-type-agreement)
11. [Graph Traversal](#11-graph-traversal)
12. [Enumerations](#12-enumerations)
13. [LLM Integration Details](#13-llm-integration-details)
14. [Summary Files](#14-summary-files)
15. [Developer Notes & Known Gaps](#15-developer-notes--known-gaps)

---

## 1. Project Layout

```
.
├── src/
│   ├── main.py                        # FastAPI app factory & lifespan
│   ├── config/
│   │   └── settings.py                # Pydantic-settings singleton
│   ├── controllers/
│   │   ├── router.py                  # Central route registry (/api/v1)
│   │   ├── health_controller.py       # GET /health, /health/ready
│   │   ├── ingestion_controller.py    # POST /ingest/file, DELETE /ingest/collection
│   │   └── retrieval_controller.py    # POST /query, POST /query/agentic
│   ├── enums/
│   │   ├── chunk_category.py          # KNOWLEDGE | KEYWORDS | FEATURES | WORKFLOWS | PERSONAS | ENTITIES
│   │   ├── chunk_sub_type.py          # INSTALL | CONFIGURE | TROUBLESHOOT | … (12 lifecycle values)
│   │   ├── ingestion_status.py        # PENDING | RUNNING | COMPLETED | FAILED
│   │   └── source_type.py             # PDF | TEXT | MARKDOWN | HTML | CSV | JSON
│   ├── models/
│   │   ├── chunk.py                   # Chunk + ChunkMetadata (dual-vector design)
│   │   ├── document.py                # Document + DocumentMetadata
│   │   ├── ingestion.py               # IngestResponse
│   │   ├── pipeline_context.py        # PipelineContext (ingestion run state)
│   │   ├── query.py                   # QueryRequest + QueryResult + RetrievedChunk
│   │   └── agentic.py                 # AgenticQueryRequest + AgenticAnswer + supporting types
│   ├── services/
│   │   ├── ingestion/
│   │   │   ├── entity_pipeline.py     # Orchestrates the full 9-step ingestion flow
│   │   │   ├── ingestion_service.py   # Async facade over EntityPipeline
│   │   │   ├── llm_service.py         # LLM completion pool (concurrency, retries, rate-limit)
│   │   │   ├── loaders/               # Format-specific document loaders (PDF/HTML/CSV/JSON/text)
│   │   │   ├── cleaners/              # Rule-based text cleaning & command-reference stripping
│   │   │   ├── processors/            # DocumentProcessor (normalisation pass)
│   │   │   ├── chunkers/              # Heading-tree parser + recursive paragraph chunker
│   │   │   ├── classifiers/           # ClassifyService + lifecycle taxonomy heuristics
│   │   │   ├── embedders/             # EmbeddingService (local sentence-transformers or AIM)
│   │   │   ├── prompts/               # All LLM prompts (extraction_v3, classify, distill, …)
│   │   │   ├── markdown/              # MarkdownService — per-category .md output files
│   │   │   ├── output_writer.py       # JSONL output writer
│   │   │   ├── docx_writer.py         # DOCX output writer
│   │   │   ├── summary_distiller.py   # Distil per-category summaries into summary/*.md
│   │   │   └── chunkers/strategies/   # BaseChunker + RecursiveChunker
│   │   ├── retrieval/
│   │   │   ├── retrieval_service.py   # Basic ANN + DFS tree expansion
│   │   │   ├── agentic_retrieval_service.py  # Full 5-step agentic flow
│   │   │   ├── query_understanding.py # LLM rewrite, multi-query, facet extract, synthesise
│   │   │   ├── graph_traversal.py     # DFS / BFS / ancestor traversal over Milvus
│   │   │   ├── ranking.py             # Pure ranking helpers (intent, facets, RRF, IDF)
│   │   │   └── scoring.py             # composite_score, rank_score, topic_centrality, subtype_agreement
│   │   └── vectordb/
│   │       └── milvus_service.py      # pymilvus wrapper (schema, upsert, ANN search, graph helpers)
│   └── utils/
│       ├── constants.py               # detect_source_type()
│       ├── file_utils.py              # save_upload / delete_file / get_upload_dir
│       ├── llm_helpers.py             # _is_placeholder, _make_snippet, _parse_blocks
│       ├── logging.py                 # get_logger() wrapper
│       └── providers.py              # IBM AIM HTTP provider (curl-based, SSE consumer)
├── scripts/
│   ├── probe_aim.sh                   # curl probe for AIM gateway streaming behaviour
│   └── probe_window_size.sh           # probe LLM context window limits
├── test_query/
│   ├── ui.html                        # Developer query UI (mounted at /ui)
│   └── serve.py                       # Standalone dev server for the UI
├── summary/                           # Pre-generated per-category distilled summaries
├── tests/
│   └── README.md                      # "Needs to be implemented"
├── .env.example                       # Full configuration reference
└── requirements.txt
```

---

## 2. Configuration & Environment

All configuration is driven by a single `Settings` class in [`src/config/settings.py`](src/config/settings.py). It uses **pydantic-settings** with a custom `_DotEnvSource` subclass that strips inline `# comments` from `.env` values before Literal validation runs.

Settings are loaded once at startup via an `lru_cache(maxsize=1)` singleton (`get_settings()`). A `reload_settings()` helper clears the cache for testing.

### Key setting groups

| Group | Variables | Purpose |
|---|---|---|
| **App** | `APP_NAME`, `APP_ENV`, `LOG_LEVEL`, `PRODUCT_NAME` | Identity; `PRODUCT_NAME` is the only product-specific value injected into LLM prompts |
| **Milvus** | `MILVUS_MODE` (`lite`/`standalone`), `MILVUS_HOST/PORT/USER/PASSWORD`, `MILVUS_COLLECTION`, `MILVUS_DIMENSION` | Vector store connection |
| **Embedding** | `EMBEDDING_PROVIDER` (`local`/`aim`), `EMBEDDING_MODEL_NAME`, `EMBEDDING_BATCH_SIZE`, `EMBEDDING_DELAY` | Embedding model selection |
| **LLM** | `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`, `LLM_ENABLED` | IBM AIM / Watsonx endpoint |
| **Token budget** | `LLM_INPUT_WINDOW_TOKENS` (8k), `LLM_MAX_OUTPUT_TOKENS` (32k), `LLM_MAX_TOKENS` (legacy alias) | Controls per-call context split; keeping input small avoids the "30× chunk regression" from oversized windows |
| **Extraction** | `LLM_EXTRACTION_MODE` (`all_types`/`sequential`/`parallel`/`independent`), `LLM_COMPACT_SCHEMA` | Trade quality vs. speed in entity extraction |
| **Chunking** | `CHUNK_STRATEGY`, `CHUNK_TARGET_TOKENS`, `CHUNK_CEILING_TOKENS`, `CHUNK_OVERLAP_TOKENS`, `CHARS_PER_TOKEN` | Chunker sizing |
| **Retrieval** | `SEARCH_ON_SUMMARY`, `CONTENT_FALLBACK_THRESHOLD`, `RETRIEVAL_MIN_COSINE`, `RETRIEVAL_FALLBACK_TO_BEST` | ANN search behaviour |
| **Scoring** | `SCORE_W_SUMMARY`, `SCORE_W_CONTENT`, `SCORE_W_FACET`, `COS_FLOOR`, `COS_CEIL` | Composite score weights and calibration band |
| **Cleaning** | `STRIP_COMMAND_REFERENCE`, `COMMAND_REF_DENSITY`, `COMMAND_REF_MIN_LINES` | Heuristic command-dump stripping |
| **Storage** | `UPLOAD_DIR`, `MAX_UPLOAD_SIZE_MB`, `JSONL_OUTPUT_DIR`, `MD_OUTPUT_DIR`, `SUMMARY_DIR` | File output paths |
| **Debug** | `LLM_DEBUG_RAW_DIR`, `LLM_DEBUG_MIN_CHARS` | Raw LLM response dumps for parse failures |

> **Critical note on `LLM_INPUT_WINDOW_TOKENS`:** increasing it dramatically _reduces_ chunk count. At 8k tokens (~24k chars), a large document produces ~241 windows and ~4,120 chunks. At 32k tokens it produces ~13 windows and ~132 chunks. Keep input small; raise `LLM_MAX_OUTPUT_TOKENS` independently.

---

## 3. Application Entry Point

[`src/main.py`](src/main.py) is the FastAPI app factory.

**`create_app()`** performs:
1. Reads `Settings` and configures `FastAPI` metadata (title, description, version, docs URLs).
2. Adds `CORSMiddleware`. In non-production, `allow_origin_regex=r".*"` echoes back the concrete requesting origin — satisfying both the browser's CORS check and `allow_credentials=True` without the forbidden `*`/credentials combination.
3. Mounts `api_router` (all routes under `/api/v1`).
4. Optionally serves `test_query/ui.html` as a static file at `/ui`.

The **lifespan** context manager initialises the upload directory on startup and logs shutdown.

---

## 4. API Surface

All routes are prefixed `/api/v1` via the central [`src/controllers/router.py`](src/controllers/router.py).

### Health

| Method | Path | Description |
|---|---|---|
| `GET` | `/api/v1/health` | Liveness probe — always 200 if the process is up |
| `GET` | `/api/v1/health/ready` | Readiness probe — 200 when Milvus is reachable, 503 otherwise |

### Ingestion

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/v1/ingest/file` | Upload a file (PDF, TXT, MD, HTML, CSV, JSON). Max size from `MAX_UPLOAD_SIZE_MB`. Returns `202 Accepted` with an `IngestResponse` |
| `DELETE` | `/api/v1/ingest/collection` | Drop the entire Milvus collection (recreated automatically on next ingest) |

### Retrieval

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/v1/query` | Basic ANN search. Accepts `QueryRequest` (`query`, `top_k`, `filter_category`, `score_threshold`, `use_dfs`). Returns `QueryResult` |
| `POST` | `/api/v1/query/agentic` | Full agentic flow. Accepts `AgenticQueryRequest`. Returns `AgenticAnswer` with answer text, supporting chunks, matched workflows, plan steps, facets, and trace log |

Interactive API docs: `/docs` (Swagger UI), `/redoc`.

---

## 5. Data Model

### `Chunk` ([`src/models/chunk.py`](src/models/chunk.py))

The core unit of storage. Every chunk carries **two independent vector spaces**:

| Field | Type | Purpose |
|---|---|---|
| `chunk_id` | `str` (UUID) | Primary key |
| `content` | `str` | Verbatim extracted text |
| `content_hash` | `str` | SHA-256 of content — deduplication / change detection |
| `summary` | `str` | Abstractive gist (LLM-generated or extractive fallback) |
| `embedding` | `list[float]` | Dense vector of `content` |
| `summary_embedding` | `list[float]` | Dense vector of `summary` (name-prefixed) |
| `keywords/features/workflows/personas/entities` | `list[str]` | LLM-extracted cross-category links + lexical anchors |
| `metadata` | `ChunkMetadata` | `chunk_type`, `sub_type`, `headings`, `depth`, `is_leaf`, `parent_id`, `children_ids` |

The `token_count` is a `@computed_field` (`len(content) / 4.5`).

### `ChunkMetadata`

Structural and semantic metadata kept separate from content:

- **`depth`** — tree depth (1=root, 2=section, 3=subsection, up to 6).
- **`is_leaf`** — True when this chunk carries actual content (not just a heading anchor).
- **`parent_id` / `children_ids`** — full N-level tree linkage enabling DFS/BFS graph traversal at retrieval time.
- **`headings`** — breadcrumb from root to this node, e.g. `["Installing S-TAP", "Prerequisites"]`.

### `AgenticAnswer` ([`src/models/agentic.py`](src/models/agentic.py))

The response type for the agentic query endpoint. Contains:
- `query`, `rewritten_query`, `multi_queries` — the query and all its reformulations
- `intent` — `INFORMATIONAL` | `ACTION`
- `facets` — extracted keywords, personas, features, entities
- `facet_details` — per-category chunks retrieved for each facet
- `answer` — synthesised text (LLM or extractive fallback)
- `supporting_chunks` — all chunks that contributed to the answer
- `matched_workflows` — workflow matches (action branch only)
- `selected_workflow` — top workflow match
- `plan` — structured `PlanStep` list (action branch only)
- `trace` — step-by-step execution log for debugging
- `retrieval_top_score` — highest cosine seen across all searches

---

## 6. Ingestion Pipeline

Entry point: [`IngestionService.ingest()`](src/services/ingestion/ingestion_service.py) wraps `EntityPipeline.run()` in `asyncio.to_thread` so the FastAPI event loop is never blocked.

### 6.1 Document Loaders

[`src/services/ingestion/loaders/`](src/services/ingestion/loaders/)

A registry pattern (`_REGISTRY` dict in [`loader.py`](src/services/ingestion/loaders/loader.py)) maps each `SourceType` to a loader class. All loaders extend `BaseLoader` from [`formats/base.py`](src/services/ingestion/loaders/formats/base.py) and return a `Document`.

| Source type | Loader | Library |
|---|---|---|
| `PDF` | `PDFLoader` | `pdfplumber` (font-aware heading detection) |
| `TEXT` / `MARKDOWN` | `TextLoader` | stdlib |
| `HTML` | `HTMLLoader` | `beautifulsoup4` + `lxml` |
| `CSV` | `CSVLoader` | stdlib `csv` |
| `JSON` | `JSONLoader` | stdlib `json` |
| `S3` | (via `formats/s3.py`) | `boto3` |

To add a new format: create `formats/<name>.py` extending `BaseLoader`, add the mapping to `_REGISTRY`, and add the new `SourceType` enum value.

### 6.2 Text Cleaning

[`src/services/ingestion/cleaners/`](src/services/ingestion/cleaners/)

Two cleaning passes:

**Pass A — Rule-based** (`DocumentProcessor` in [`processors/document_processor.py`](src/services/ingestion/processors/document_processor.py)):
- Non-ASCII → ASCII normalisation, deduplication, whitespace normalisation.

**Command-reference stripping** (`text_cleaner.py`, `command_reference.py`):
- Controlled by `STRIP_COMMAND_REFERENCE`, `COMMAND_REF_DENSITY`, `COMMAND_REF_MIN_LINES`.
- Drops blocks that look like CLI/REST reference dumps (high ratio of command-line patterns per line). Implemented as a shape-based heuristic — no product-specific patterns.

**Pass B — LLM cleaning** (disabled by default: `LLM_CLEAN_ENABLED=false`):
- Strips residual page noise, rejoins hyphen-split words, fixes OCR artefacts per window. Disabled because the output budget (8k tokens) is too small to reproduce a 24k-char window faithfully — every window fell back, wasting ~563 extra LLM calls with no quality gain.

### 6.3 LLM Service & Windowing

[`src/services/ingestion/llm_service.py`](src/services/ingestion/llm_service.py) and [`src/utils/providers.py`](src/utils/providers.py)

The raw document text is sliced into **windows** before LLM processing. Window size is `LLM_INPUT_WINDOW_TOKENS × CHARS_PER_TOKEN` (defaults: 8,000 tokens × 3.0 chars/token = 24,000 chars per window).

`LLMService` manages a concurrent pool of HTTP calls (`LLM_CONCURRENCY`, default 8) with:
- Exponential backoff retries on transient errors (429, 5xx, timeouts).
- `_PermanentError` / `_TransientError` sentinel types to avoid retrying 401/403.
- `_FAILFAST_AFTER=20` — aborts a batch if 20 consecutive requests fail without a single success.
- Raw response dumps to `LLM_DEBUG_RAW_DIR` for the first 5 parse failures per process.
- `LLM_REQUEST_DELAY` inter-window delay as a rate-limit guard.

The provider uses `/usr/bin/curl` (not the Python `httpx` client) to avoid Akamai TLS fingerprint blocking in front of the IBM AIM gateway. It writes the request body to a temp file and uses `curl -d @file` — bypassing the WAF trigger that shell-level JSON injection would cause.

**Extraction modes** (`LLM_EXTRACTION_MODE`):

| Mode | Description | Speed |
|---|---|---|
| `all_types` | One LLM call per window extracts all 6 entity types simultaneously | Fastest |
| `sequential` | ROUTER call per window identifies categories present, then one typed pass per category | Slowest, highest fidelity |
| `parallel` | ROUTER call per window, then all typed passes dispatched into one LLM pool concurrently | Same call count as sequential, wall-clock ≈ `all_types` |
| `independent` | No ROUTER. 6 direct per-category passes per window in parallel, each with its own type-specific prompt | No router overhead; same parallelism as `parallel` |

### 6.4 Entity Extraction (EntityPipeline)

[`src/services/ingestion/entity_pipeline.py`](src/services/ingestion/entity_pipeline.py)

The complete 9-step pipeline:

```
1. load          → Document (format-specific loader)
2. clean pass A  → DocumentProcessor (rules, dedup, normalise)
3. window        → slice text into LLM context windows
4. clean pass B  → LLM per window (disabled by default)
5. LLM extract   → typed chunks + sub_type + relations + summary per window
6. rechunk       → RecursiveChunker re-splits LLM output into final leaf chunks
7. summarise     → SummarizerService gives each new leaf its own summary
8. embed         → EmbeddingService (content + summary vectors for every chunk)
9. persist       → Markdown .md + JSONL + Milvus
```

**Tree wiring:** Each window produces one root `knowledge` chunk (depth=1). Every other entity extracted from that window becomes its child (depth=2). `parent_id` / `children_ids` are wired bidirectionally, enabling DFS/BFS at retrieval time.

**Extraction prompts** live in [`src/services/ingestion/prompts/extraction_v3.py`](src/services/ingestion/prompts/extraction_v3.py):
- `ALL_TYPES_SYSTEM` / `ALL_TYPES_SYSTEM_COMPACT` — single-pass all-types extraction
- `TYPE_PROMPTS` — per-category typed prompts for `sequential`/`parallel`/`independent` modes
- `ROUTER_SYSTEM` / `ROUTER_USER` — router call that identifies which categories are present
- `build_domain_profile()` — injects `PRODUCT_NAME` from settings into every prompt

### 6.5 Chunking Strategies

[`src/services/ingestion/chunkers/`](src/services/ingestion/chunkers/)

The primary strategy is **`RecursiveChunker`** ([`strategies/recursive_chunker.py`](src/services/ingestion/chunkers/strategies/recursive_chunker.py)), a paragraph-preserving hierarchical chunker:

1. Parses the document into a heading tree (`HeadingNode`) via [`heading_tree.py`](src/services/ingestion/chunkers/heading_tree.py).
2. Each heading gets an **anchor chunk** (title only, is_leaf=False if it has body or children).
3. The heading's body is split on `\n\n` boundaries into **paragraph leaf chunks** (parented to the anchor).
4. Child headings recurse as their own anchor→paragraph subtrees.
5. Every chunk content is prefixed with the heading breadcrumb (`"H1 > H2 > H3"`) so it is self-describing when retrieved in isolation.

`_backfill_children()` populates `children_ids` on every parent after the full tree is built.

The chunker also has a `splitter.py` (fixed-size overlap splitting) and `semantic_chunker.py` as alternatives, but the recursive strategy is the default and recommended path.

### 6.6 Classification & Summarization

[`src/services/ingestion/classifiers/classify_service.py`](src/services/ingestion/classifiers/classify_service.py)

`ClassifyService.classify_and_summarize()` runs one LLM pass over all chunks to assign:
- **`categories`** — one or more of the 6 `ChunkCategory` values
- **`sub_type`** — one of the 12 `ChunkSubType` lifecycle values
- **`summary`** — 1–2 sentence extractive/abstractive summary
- **facets** — `keywords`, `features`, `workflows`, `personas`, `entities` (cross-category links + lexical anchors)

**Fallbacks:**
- If LLM is disabled or fails, `classify_sub_type()` in [`classifiers/taxonomy.py`](src/services/ingestion/classifiers/taxonomy.py) assigns a heuristic sub_type from heading/content patterns.
- An extractive summary (first 2 sentences) is used if LLM returns nothing.
- Category defaults to `KNOWLEDGE` if not parseable.

### 6.7 Embedding Service

[`src/services/ingestion/embedders/embedding_service.py`](src/services/ingestion/embedders/embedding_service.py)

Two providers, selected by `EMBEDDING_PROVIDER`:

**`local` (default):** `_LocalProvider` runs `sentence-transformers` on-device (Apple MPS or CPU). Zero network calls — immune to WAF blocks and rate limits. Recommended for production.

**`aim`:** `_AIMProvider` calls the IBM AIM `/inference/embeddings` endpoint via `/usr/bin/curl`. Has a 500-token truncation guard and exponential-backoff retries (3 attempts with `2^attempt` second delays). Falls back when local model is unavailable.

**Embedding strategy for summaries:**  
`_embed_text()` prepends the section name to the summary before embedding (e.g. `"S-TAP agent: …"`). This means a query naming the item directly (`"What is S-TAP?"`) matches even when the summary phrasing uses different vocabulary. The stored `chunk.summary` is unchanged; only the embedded string carries the prefix.

**Two vectors per chunk:**
- `chunk.embedding` — vector of the raw `content` (for content-similarity fallback)
- `chunk.summary_embedding` — vector of the name-prefixed summary (primary search target)

### 6.8 Output Writers

After embedding, the pipeline writes three output formats:

| Output | File | Content |
|---|---|---|
| **Markdown** | `output/<CATEGORY>.md` | Per-category grouped summaries |
| **JSONL** | `output/chunks_<cat>.jsonl` | Structured chunk records |
| **Milvus** | Collection `MILVUS_COLLECTION` | 14-field schema with both vector fields |
| **Distilled summaries** | `uploads/summary/<CATEGORY>.md` | Concise per-category knowledge base overview files used by the agentic retriever as grounding context |

---

## 7. Vector Store (Milvus)

[`src/services/vectordb/milvus_service.py`](src/services/vectordb/milvus_service.py)

`MilvusService` is a thin `pymilvus` wrapper supporting both **Milvus Lite** (embedded, local file) and **Milvus Standalone** (remote Docker container).

### Collection schema (14 fields)

| Field | Type | Notes |
|---|---|---|
| `chunk_id` | `VARCHAR(64)` | Primary key (UUID) |
| `chunk_type` | `VARCHAR(32)` | `ChunkCategory` value |
| `sub_type` | `VARCHAR(32)` | `ChunkSubType` value |
| `depth` | `INT32` | Tree depth (1–6) |
| `is_leaf` | `BOOL` | Leaf vs. anchor chunk |
| `parent_id` | `VARCHAR(64)` | Parent chunk UUID |
| `children_ids` | `VARCHAR(2048)` | JSON-encoded `list[str]` |
| `content_hash` | `VARCHAR(64)` | SHA-256 for deduplication |
| `headings` | `VARCHAR(1024)` | JSON-encoded breadcrumb list |
| `content` | `VARCHAR(65535)` | Full verbatim text |
| `summary` | `VARCHAR(8192)` | Abstractive gist |
| `questions` | `VARCHAR(4096)` | JSON list of hypothetical questions |
| `embedding` | `FLOAT_VECTOR(dim)` | Content vector |
| `summary_embedding` | `FLOAT_VECTOR(dim)` | Summary vector |

Both vector fields are indexed with **HNSW** (`M=16`, `efConstruction=200`, metric `COSINE`).

### Key operations

- **`upsert_chunks()`** — batched upsert (200 rows/batch) to stay under the 64 MB gRPC limit. Auto-recreates the collection if it is missing during upsert.
- **`search()`** — ANN search over either `embedding` or `summary_embedding` (chosen by `SEARCH_ON_SUMMARY` or caller override). `ef=64` at query time.
- **`fetch_by_ids()`** — exact primary-key lookup for graph traversal.
- **`fetch_ancestors()`** — walks `parent_id` chain up to the root.
- **`fetch_subtree()`** — iterative DFS downward through `children_ids`, bounded by `max_nodes=128`.
- **`drop_collection()`** / **`get_collection_stats()`** — maintenance operations.

**Auto-heal:** On connection in `standalone` mode, `_ensure_docker_running()` checks if the Milvus port is reachable and runs `docker start milvus-standalone` with a 30-second wait if it isn't. This guards against the etcd lease-expiry crash observed in practice.

---

## 8. Retrieval — Basic Path

[`src/services/retrieval/retrieval_service.py`](src/services/retrieval/retrieval_service.py)

`RetrievalService.query()` implements the simple top-K ANN path:

1. Build a Milvus `filter_expr` from `filter_category` if supplied.
2. Embed the query with `EmbeddingService.embed_query()`.
3. Call `MilvusService.search()` — returns scored `RetrievedChunk` list.
4. Optionally expand each hit with DFS (`use_dfs=True`): for each hit, fetch ancestor path (heading breadcrumb) and full descendant subtree.
5. Return `QueryResult(query, results, total)`.

This path is intentionally minimal — no rewriting, no facet extraction, no LLM synthesis.

---

## 9. Retrieval — Agentic Path

[`src/services/retrieval/agentic_retrieval_service.py`](src/services/retrieval/agentic_retrieval_service.py)

`AgenticRetrievalService.run()` implements the full 5-step "whiteboard" pipeline. All heavy dependencies (`EmbeddingService`, `MilvusService`, `QueryUnderstanding`) are constructor-injectable for offline testing.

### 9.1 Step 1: Query Rewrite & Multi-Query Expansion

The user's question is rewritten using two context sources:
- **`KNOWLEDGE.md`** — the distilled per-category summary file for grounding.
- **`ENTITIES.md`** — entity list for acronym expansion.
- **Top 4 KNOWLEDGE vector chunks** via ANN search.

`QueryUnderstanding.rewrite_query()` expands acronyms, adds entity names, and critically **preserves question type** — a `"what is"` question stays as `"what is"` so the retriever knows a definition is expected, not a procedure.

**Pronoun-only detection:** Queries like `"How do I set it up?"` (no referent) bypass LLM rewriting entirely — the LLM would hallucinate a subject, producing a worse embedding than the original.

**Multi-query expansion:** `generate_multi_queries()` asks the LLM to produce 4 query variants covering 4 orthogonal angles:
1. Synonym / paraphrase
2. Concept / definition
3. Procedure / task
4. Entity / relation

The final `multi_queries` list = `[original, rewritten, variant_1, …, variant_4]` (deduplicated, order-preserved).

### 9.2 Step 2: Facet Extraction

`extract_facets()` sends the rewritten query + labelled MD examples (real terms from the KB) to the LLM and extracts JSON:

```json
{"keywords": [...], "personas": [...], "features": [...], "entities": [...]}
```

- **`keywords`** — product-specific acronyms and component names from the KB (e.g. `"S-TAP"`, `"GIM"`)
- **`personas`** — user roles implied by the question (e.g. `"Database Administrator"`)
- **`features`** — product capability areas referenced (e.g. `"Threat Detection"`)
- **`entities`** — named system objects (e.g. `"collector"`, `"policy"`)

Fallback: if LLM is disabled, runs semantic search per category and uses the top-hit labels.

### 9.3 Step 3: Facet Detail Fetch (RRF)

`_fetch_facet_details()` fetches detailed chunks for each facet category using **RAG-Fusion** (`_rrf_search()`):

**Reciprocal Rank Fusion (RRF):**
1. Run one ANN search per query variant **concurrently** (`asyncio.gather`).
2. Merge result lists with RRF: `score(d) = Σ 1/(k + rank_q(d))` where `k=60`.
3. Apply intent-aware block bias — preferred categories for the detected intent get a `+15%` RRF score nudge.
4. Write the fused RRF score back to `chunk.score` (preserving raw cosine in `summary_cos`).

Optionally expands each ANN hit with BFS neighbourhood (`TraversalStrategy.BFS` or `BOTH`).

### 9.4 Step 4: Intent & Sub-type Detection

**Intent:** `ranking.detect_action_intent()` is a heuristic classifier that returns `("action" | "informational", confidence)`:
- Action vocabulary: `_ACTION_VERBS` set + `_ACTION_PHRASES` list.
- Informational signals: leading `"what is"`, `"why"`, `"explain"`, `"define"` phrases.
- Score accumulates to 1.0; threshold for `"action"` is `>= 0.5`.
- `force_intent` on the request bypasses this detection.

**Sub-type (lifecycle scope):** `detect_query_sub_type()` in [`classifiers/taxonomy.py`](src/services/ingestion/classifiers/taxonomy.py) maps the query to one of the 12 `ChunkSubType` values. This scopes action retrieval — `"how to configure collector?"` fetches only `configure`-sub-typed personas, features, and workflows.

### 9.5 Step 5a: Informational Branch

Triggered when `intent == INFORMATIONAL`.

1. `_rrf_search()` over `multi_queries` restricted to `_INFORMATIONAL_CATS` = `[knowledge, features, entities, keywords]` — **workflows are excluded** (they are procedural, not definitional).
2. Optionally expand each hit with DFS (descendants + ancestor breadcrumb) and/or BFS neighbourhood.
3. Merge all facet-detail chunks gathered in step 3.
4. **Re-score** with `ranking.rescore_and_rank()` (IDF-weighted composite + topic-centrality ordering).
5. Build context text: `KNOWLEDGE.md` grounding + chunk content + summary + facet blocks.
6. Call `QueryUnderstanding.synthesize_answer()` — sends context to LLM with the `_ANSWER_SYSTEM` prompt.
7. Clean the LLM output (strip `window-NNN` identifiers, table junk, `"Based on context..."` preamble).
8. Fall back to `ranking.assemble_answer()` (extractive stitching) if LLM is disabled.

### 9.6 Step 5b: Action Branch

Triggered when `intent == ACTION`.

1. **Sub-type scoped fetch:** if a lifecycle sub-type was detected, run `_fetch_sub_type_scoped()` — fetches personas, features, and workflows filtered to that sub-type only via RRF.
2. **Build workflow query:** original + `" :: "` + all facet terms.
3. **Workflow RRF search:** `_rrf_search()` over `[multi_queries + wf_query + kb_ctx_query]` restricted to `ChunkCategory.WORKFLOWS` with `intent_label="action"`. Falls back to unscoped if sub-type scoping yields nothing.
4. **Facet-boosted re-ranking:** `ranking.rerank_by_facets()` applies a `0.15` boost per fraction of extracted facet terms present in the chunk content.
5. **DFS step extraction:** for each matched workflow, `_graph.dfs(hit.chunk_id)` fetches the ordered subtree, and `ranking.extract_workflow_steps()` converts it to a step list.
6. **Enrichment context:** RRF over `_INFORMATIONAL_CATS + [personas]` using all query variants — produces Knowledge + Keywords + Features + Entities + Personas chunks.
7. **Plan synthesis:** `QueryUnderstanding.synthesize_plan(workflow_name, steps, context)` calls the LLM with `_PLAN_SYSTEM` and returns a structured JSON plan `[{"action": ..., "detail": ...}]`. Falls back to `synthesize_answer(context)` when no steps are found.

---

## 10. Scoring & Ranking

[`src/services/retrieval/scoring.py`](src/services/retrieval/scoring.py) and [`ranking.py`](src/services/retrieval/ranking.py)

The scoring system deliberately separates **display score** from **ordering score**:

> "Calibrating a cosine changes the displayed value but not the order, so a pretty number on a wrongly-ranked chunk is worse than useless."

### 10.1 Composite Score

`composite_score(query, summary_cos, content_cos, facets, weights, df, n_docs, floor, ceil)` returns a `ScoreBreakdown`:

```
score = w_summary × norm(summary_cos) + w_content × norm(content_cos) + w_facet × facet_match
```

- **`norm(cos)`** — linearly rescales the raw cosine from `[COS_FLOOR, COS_CEIL]` onto `[0, 1]`. Default band: `[0.40, 0.85]` for `multi-qa-MiniLM-L6-cos-v1`.
- Default weights: `w_summary=0.75`, `w_content=0.25`, `w_facet=0.00` (facet excluded from composite — it is used only in ranking).
- Returns `ScoreBreakdown` with `raw_summary_cos`, `raw_content_cos`, `summary_norm`, `content_norm`, `facet` for inspection.

### 10.2 Rank Score

`rank_score(query, summary_cos, facets, chunk_sub_type, df, n_docs)`:

```
rank = (0.45 × sem + 0.20 × fac + 0.35 × centrality) × subtype_agreement
```

Where `sem = norm(summary_cos)`, `fac = facet_match(…)`, `centrality = topic_centrality(…)`.

### 10.3 Topic Centrality

`topic_centrality()` answers: **"Is this section _about_ the query subject, or does it just _mention_ it?"**

Computes:
- **coverage** — IDF-weighted fraction of query terms found in the section title
- **focus** — fraction of the title's terms that are query terms (short, focused titles win)
- `score = coverage × (0.5 + 0.5 × focus)`
- **Penalty:** titles matching `_PROBLEM_TITLE` (containing "not", "failed", "error", "troubleshoot", etc.) get `× 0.35` — prevents `"S-TAP is not capturing traffic"` from ranking above `"What is S-TAP?"` for a definition query.

**IDF weighting:** `_idf_weight(term, df, n_docs) = log(1 + (n - df + 0.5) / (df + 0.5))` — rare terms ("S-GATE") score far higher than common terms ("configure"). `df` is computed over the candidate set as a cheap approximation of corpus-level document frequency.

### 10.4 Sub-type Agreement

`subtype_agreement(query, chunk_sub_type)` returns a multiplier:

| Scenario | Multiplier |
|---|---|
| Sub-types match exactly | `1.0` |
| Definitional question + `overview`/`reference` chunk | `1.0` |
| Definitional question + `troubleshoot` chunk | `0.25` |
| Action question + `troubleshoot` chunk | `0.35` |
| All other mismatches | `0.6` |

This fixed the measured failure where `"What does S-TAP stand for?"` returned a `troubleshoot` page (`"Rules of Failover"`) instead of the definition.

---

## 11. Graph Traversal

[`src/services/retrieval/graph_traversal.py`](src/services/retrieval/graph_traversal.py)

`ChunkGraphTraversal` is a stateless helper bound to any `_NodeReader` (duck-typed, so it works with fakes in tests).

| Method | Algorithm | Use case |
|---|---|---|
| `dfs(root_id)` | Iterative pre-order DFS via explicit stack | Reconstruct ordered workflow steps (Step 1→2→3) |
| `bfs(root_id)` | Level-order BFS; fetches entire frontier per level | Level-by-level subtree exploration |
| `bfs_neighborhood(seed_ids, hops)` | Undirected BFS: children + parent per node | Gather breadth-of-related-context (siblings, parent) |
| `ancestors(chunk_id)` | Iterative `parent_id` chain walk | Heading breadcrumb for context |

All traversals are bounded (`max_nodes`, `max_depth`) to prevent runaway Milvus queries.

---

## 12. Enumerations

### `ChunkCategory` ([`src/enums/chunk_category.py`](src/enums/chunk_category.py))

The primary classification axis — **what type of information is this?**

| Value | Meaning |
|---|---|
| `knowledge` | General factual/conceptual content (catch-all — nothing is lost) |
| `keywords` | Product-specific terms, acronyms, component names |
| `features` | Product capabilities and feature areas |
| `workflows` | Ordered procedures, how-to steps, runbooks |
| `personas` | User roles and their responsibilities |
| `entities` | Named system objects (collectors, policies, agents) |

### `ChunkSubType` ([`src/enums/chunk_sub_type.py`](src/enums/chunk_sub_type.py))

The secondary classification axis — **which lifecycle stage is this content about?** (orthogonal to category)

`install` | `uninstall` | `upgrade` | `configure` | `integrate` | `administer` | `monitor` | `troubleshoot` | `use` | `reference` | `overview` | `other`

This drives **action-scoped retrieval**: `"how to configure collector?"` fetches only `configure`-labelled chunks, preventing install or troubleshoot content from polluting a configuration answer.

---

## 13. LLM Integration Details

The LLM is an **IBM AIM** (AI Model) gateway backed by Watsonx `granite-4-h-small` (or any OpenAI-compatible model).

### Transport quirks

The codebase documents several hard-won lessons about the IBM AIM gateway:

- **curl over httpx:** All LLM calls use `/usr/bin/curl` via `subprocess`. The Python `httpx` client triggers Akamai TLS fingerprint detection; curl does not.
- **Streaming disabled by default (`LLM_STREAM=false`):** The gateway's SSE implementation for `gpt-oss-120b` was observed to emit only the first few tokens and close — a complete response on the wire but cut off at the application level. Non-streaming returns full JSON in 0.7–1.2s.
- **HTTP/1.1 (`LLM_HTTP_VERSION=1.1`):** HTTP/2 multiplexing can produce mid-stream `RST_STREAM` behind a CDN/ingress, truncating SSE responses. HTTP/1.1 has no stream-reset path.
- **Watsonx hard cap:** 100,000 new tokens per request. `_safe_max_tokens()` in `providers.py` enforces `min(llm_max_output_tokens, 100_000, context_budget)`.
- **`LLM_STREAM_REQUIRE_DONE=true` (but effectively ignored when streaming is off):** Watsonx/vLLM does not send the OpenAI `data: [DONE]` SSE sentinel. Requiring it caused every window to fail with "truncated" on complete responses.

### Prompt engineering

All prompts in [`src/services/ingestion/prompts/`](src/services/ingestion/prompts/) and [`query_understanding.py`](src/services/retrieval/query_understanding.py) are data-source independent. The only product-specific injection is `PRODUCT_NAME` from settings, which is interpolated into the system prompts at construction time via `_read_product_name()` (read from the first heading of any summary `.md` file — never hardcoded).

### Heuristic fallbacks

Every LLM call site has a deterministic fallback:
- Query rewrite → return original query
- Facet extraction → semantic search per category
- Answer synthesis → `ranking.assemble_answer()` (extractive stitching)
- Plan synthesis → `synthesize_answer()` (free-form LLM answer)
- Classification → extractive summary + heuristic `classify_sub_type()`

This means the entire pipeline runs offline with `LLM_ENABLED=false`, which is essential for testing and local development.

---

## 14. Summary Files

After ingestion, `SummaryDistiller` writes per-category Markdown files to `uploads/summary/`:

```
uploads/summary/
├── KNOWLEDGE.md
├── KEYWORDS.md
├── FEATURES.md
├── WORKFLOWS.md
├── PERSONAS.md
└── ENTITIES.md
```

These files serve as the **knowledge base overview** read by the agentic retriever:
- `KNOWLEDGE.md` + `ENTITIES.md` → rewrite context for step 1
- All six → example blocks fed to facet extraction in step 2
- `WORKFLOWS.md` → workflow grounding in the action branch

Each file has a standard 4-line header (title, blank, metadata, `---`) that `_read_summary_file()` strips before use.

The pre-generated copies in [`summary/`](summary/) represent a completed ingestion run and serve as a reference baseline.

---

## 15. Developer Notes & Known Gaps

### What is solid

- **Dual-vector architecture** (content + summary embeddings) with automatic summary→content fallback.
- **RAG-Fusion** over multiple query variants with RRF, intent-aware block bias, and score write-back.
- **Graph-aware retrieval** — DFS for ordered workflow steps, BFS for related-context breadth, ancestor walks for heading breadcrumbs.
- **IDF-weighted composite scoring** with topic-centrality to distinguish "section about X" from "section mentioning X".
- **Sub-type agreement scoring** to prevent install/troubleshoot pages from answering configure/definition queries.
- **Fully offline fallbacks** — entire pipeline runs with `LLM_ENABLED=false`.
- **Documented operational failure modes** — extensive inline comments capture exactly what broke and why the current approach works.

### Known gaps

| Gap | Detail |
|---|---|
| **No tests** | `tests/README.md` says _"Needs to be implemented"_. No unit, integration, or regression tests exist |
| **No auth** | No API key guard or rate limiting on any endpoint |
| **No CI/CD** | No Dockerfile, no `docker-compose`, no GitHub Actions workflow |
| **No async ingestion queue** | Ingestion is synchronous inside `asyncio.to_thread` — no job queue, no status-polling endpoint, no persistence for long-running runs |
| **Global service singletons** | `_basic_svc` and `_agentic_svc` in `retrieval_controller.py` are module-level globals, not dependency-injected |
| **Skeletal README** | The project `README.md` is two lines |
| **AIM provider via curl subprocess** | Works around TLS fingerprinting but creates temp files per request and spawns processes — not ideal for high-throughput production |
| **`score_w_facet=0.00` in default settings** | The facet term is effectively disabled in the composite score (but active in `rank_score` via `facet_match`) — the `.env.example` shows `0.25`, which disagrees with `settings.py` defaults |

### Running locally

```bash
# 1. Copy and fill in credentials
cp .env.example .env

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Milvus (standalone, Docker)
docker run -d --name milvus-standalone -p 19530:19530 milvusdb/milvus:latest

# 4. Start the API
uvicorn src.main:app --reload

# 5. Open the developer query UI
open http://localhost:8000/ui

# 6. Ingest a document
curl -X POST http://localhost:8000/api/v1/ingest/file \
  -F "file=@/path/to/document.pdf"

# 7. Query
curl -X POST http://localhost:8000/api/v1/query/agentic \
  -H "Content-Type: application/json" \
  -d '{"query": "What is S-TAP?", "use_llm": true}'
```

---

*This document was generated from source by reading every significant file in the codebase. Keep it in sync when the pipeline stages, schema, or scoring logic change.*
