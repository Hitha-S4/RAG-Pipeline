# Resume — GenAI RAG Pipeline Project

> Copy-paste ready bullets, tailored for different resume contexts.
> Swap in your own metrics if you have them (chunk counts, latency numbers, doc corpus size).

---

## One-Line Project Summary

> Use this in the **Projects** section header or as a tagline under the project title.

**GenAI RAG Pipeline** — Production-oriented Retrieval-Augmented Generation backend with agentic query planning, dual-vector retrieval, and LLM-powered document intelligence; built on FastAPI, Milvus, and a modern LLM provider.

---

## Single Bullet (≤ 3 lines)

> Use anywhere space is at a premium — a LinkedIn experience entry, a line in a summary, or a recruiter-screen version.

Engineered a production RAG pipeline on FastAPI, Milvus, and a modern LLM provider — covering a 9-stage ingestion flow (LLM entity extraction, hierarchical chunking, dual-vector embedding) through to an agentic retrieval engine that rewrites queries, fuses multi-variant results via Reciprocal Rank Fusion, detects user intent, and delivers synthesised answers or step-by-step execution plans accordingly.

---

## Project Entry (Projects Section)

```
GenAI RAG Pipeline                                                    Python · FastAPI · Milvus · Watsonx
IBM Guardium Documentation Intelligence                                               [link to repo/demo]
```

- Designed and built an end-to-end RAG ingestion and retrieval service for IBM Guardium Data Protection technical documentation, ingesting PDF, HTML, Markdown, CSV, and JSON sources into a Milvus vector store
- Implemented a **9-stage ingestion pipeline**: document loading → rule-based cleaning → LLM windowing → entity extraction → hierarchical recursive chunking → LLM classification → dual-vector embedding → JSONL/Markdown output → Milvus upsert
- Engineered a **dual-vector architecture** storing both a content embedding and a name-prefixed summary embedding per chunk, enabling semantic search against exact wording _and_ high-level meaning simultaneously
- Built a **full agentic retrieval flow** (5 steps): LLM query rewrite with KB grounding → multi-query expansion → RAG-Fusion over query variants using Reciprocal Rank Fusion (RRF) → heuristic intent detection → intent-branched answer synthesis (informational) or DFS workflow step extraction and structured plan generation (action)
- Designed a **composite relevance scoring system** separating display score (calibrated cosine normalisation) from ordering score (IDF-weighted facet overlap + topic-centrality + sub-type agreement), fixing the documented failure where troubleshooting pages ranked above definition pages for "what is X?" queries
- Implemented **graph-aware retrieval** over the chunk tree stored in Milvus: DFS for reconstructing ordered workflow steps, BFS neighbourhood for breadth-of-context, and ancestor walks for heading breadcrumbs
- Engineered LLM integration against IBM AIM / Watsonx via `curl` subprocess (bypassing Akamai TLS fingerprint detection), with exponential-backoff retries, streaming SSE consumption, a 100k token hard-cap guard, and raw response debug dumps — resolving multiple undocumented gateway constraints
- Ensured **full offline operation** with deterministic heuristic fallbacks at every LLM call site (query rewrite, facet extraction, answer synthesis, classification), allowing the entire pipeline to run with `LLM_ENABLED=false`

---

## Shorter Bullets (3–4 line condensed version)

> Use when the resume is tight on space.

- Built a production RAG pipeline (FastAPI + Milvus + IBM Watsonx) with a 9-stage ingestion flow covering PDF/HTML/Markdown/CSV/JSON sources, LLM entity extraction, hierarchical chunking, dual-vector embedding, and automated knowledge-base distillation
- Implemented agentic retrieval with RAG-Fusion (Reciprocal Rank Fusion over LLM-generated multi-query variants), intent detection, and intent-branched answer synthesis vs. DFS workflow-step extraction and structured plan generation
- Designed IDF-weighted composite relevance scoring with topic-centrality and lifecycle sub-type agreement, separating display calibration from result ordering to fix ranked retrieval failures at the heading level
- Resolved IBM AIM gateway constraints (Akamai TLS fingerprinting, SSE truncation, 100k token cap) and engineered a fully offline fallback path ensuring the pipeline operates without LLM access

---

## Skills to List (from this project)

```
Languages:       Python 3.11+
Frameworks:      FastAPI, Pydantic v2, pydantic-settings, asyncio
Vector DB:       Milvus (Lite + Standalone), pymilvus, HNSW indexing, ANN search
Embedding:       sentence-transformers (multi-qa-MiniLM-L6-cos-v1), HuggingFace, Apple MPS
LLM / GenAI:     IBM Watsonx (granite-4-h-small), IBM AIM gateway, OpenAI-compatible APIs
RAG Techniques:  RAG-Fusion, Reciprocal Rank Fusion (RRF), HyDE-style query expansion,
                 multi-query generation, dual-vector retrieval, summary-first ANN,
                 DFS/BFS graph traversal, IDF scoring, topic centrality
NLP:             Named entity extraction, semantic chunking, hierarchical document parsing,
                 intent classification, lifecycle sub-type detection, stop-word filtering
Document AI:     pdfplumber (font-aware heading detection), BeautifulSoup4, lxml
Cloud/Infra:     AWS S3 (boto3), Docker (Milvus standalone), REST API design
Dev tools:       uvicorn, pytest (configured), httpx, python-multipart
```

---

## Talking Points for Interviews

Use these to answer "tell me about a challenging technical problem you solved."

### 1. The dual-vector retrieval design
> "Most RAG systems store one vector per chunk. I stored two — a content vector and a name-prefixed summary vector. The summary vector matches a query against the abstract gist of a section; the content vector is a fallback for chunks whose summary is poorly worded but whose verbatim text is a strong match. The system automatically runs both passes and merges results when the top summary score falls below a calibrated threshold."

### 2. Separating display score from ordering score
> "Raw cosine from a symmetric embedding model has a compressed useful range — 0.55–0.75 for genuinely relevant pairs. Naively showing that number looks bad even when the result is correct. I separated two concepts: `composite_score()` produces a calibrated human-readable number, and `rank_score()` is what actually orders results. It combines IDF-weighted facet overlap, topic centrality (is this section _about_ the subject or just mentioning it?), and lifecycle sub-type agreement. This fixed a measured failure where 'What does S-TAP stand for?' was returning a troubleshooting page instead of the definition."

### 3. RAG-Fusion with intent-aware block bias
> "Rather than sending one query to the vector store, I generate up to 5 reformulations covering four orthogonal angles — synonym/paraphrase, concept/definition, procedure/task, entity/relation. Each variant gets its own ANN search in parallel, and the result lists are fused with Reciprocal Rank Fusion (RRF). After fusion, I apply a light block-type bias based on detected intent — so a definition question nudges knowledge/entity chunks upward, and an action question nudges workflow/feature chunks upward — before returning the top K."

### 4. Engineering around the IBM AIM gateway
> "The IBM AIM LLM gateway sits behind an Akamai CDN. Python's httpx library triggers TLS fingerprint detection and gets blocked. I switched every LLM and embedding call to use /usr/bin/curl via subprocess, writing the request body to a temp file to avoid shell-injection issues. I also discovered the gateway's SSE streaming implementation was closing after the first few tokens for large models, debugged this with probe scripts, and documented exactly when to use streaming vs. non-streaming per model. None of this was in any documentation — it came from reading raw curl output."

### 5. The recursive paragraph-preserving chunker
> "Standard fixed-size chunkers blend multiple topics into one embedding — a 3,000-token section gets one mediocre vector that scores poorly for any specific sub-topic inside it. I built a hierarchical chunker that parses the document into a heading tree, emits an anchor chunk per heading, and then splits only the body paragraphs as leaf chunks. Each leaf is prefixed with its full heading breadcrumb so it's self-describing when retrieved in isolation. This raised cosine scores by ~0.15–0.25 on targeted queries compared to the section-atomic approach."

---

## One-Paragraph Bio Version

> Use in a portfolio site, LinkedIn summary, or cover letter.

I designed and built a production-oriented RAG pipeline for IBM documentation intelligence, handling the full lifecycle from multi-format document ingestion through LLM-powered entity extraction, hierarchical paragraph-preserving chunking, dual-vector embedding, and Milvus persistence. On the retrieval side I implemented a five-step agentic flow featuring LLM query rewriting with knowledge-base grounding, RAG-Fusion over multi-query variants using Reciprocal Rank Fusion, heuristic intent detection, and intent-branched answer synthesis — informational questions produce LLM-synthesised answers, action questions produce DFS-extracted workflow steps assembled into structured execution plans. I engineered the scoring system to separate display calibration from result ordering, using IDF-weighted topic centrality and lifecycle sub-type agreement to fix concrete ranking failures. I also resolved several undocumented IBM AIM gateway constraints including Akamai TLS fingerprinting, SSE stream truncation, and the Watsonx 100k token hard cap.

---

*Tip: replace "IBM Guardium Data Protection" with "enterprise security documentation" in public versions of your resume if the project is internal.*
