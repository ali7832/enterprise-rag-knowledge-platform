# Operations Runbook

## Purpose

This service provides enterprise knowledge search and grounded answer generation through a deployable RAG API.

## Runtime Configuration

Configuration is controlled through `.env.example`:

- `RAG_ENV`: deployment environment.
- `RAG_SERVICE_NAME`: service identifier.
- `RAG_RETRIEVER_VERSION`: retriever strategy version.
- `RAG_DEFAULT_TOP_K`: default number of retrieved chunks.
- `RAG_CHUNK_SIZE`: chunk size used during local/demo indexing.
- `RAG_MINIMUM_RELEVANCE_SCORE`: grounding threshold.
- `RAG_TRACE_STORE_PATH`: JSONL query trace path.

## Query Lifecycle

1. User submits a query to `/answer`.
2. Request receives a query ID.
3. Retriever ranks indexed chunks.
4. Answer engine returns cited context.
5. Service computes grounding status and latency.
6. Query trace is written to JSONL storage.

## Demo Readiness

For hosted demos, expose `/health` and `/answer`. The health endpoint returns service name, environment, retriever version, and indexed chunk count.

## Production Roadmap

- Replace TF-IDF with hybrid dense and sparse retrieval.
- Add vector database support.
- Add tenant-aware document permissions.
- Add LLM answer synthesis with guardrails.
- Add retrieval evaluation dashboards.
- Add source refresh jobs and ingestion workers.
