# Enterprise RAG Knowledge Platform

Deployable enterprise knowledge service for retrieval-augmented answering, metadata-aware citations, query traceability, grounding checks, and API-based knowledge access.

## Core Capabilities

- Document ingestion and chunking pipeline
- Metadata-aware document and chunk schemas
- TF-IDF retrieval baseline for local/demo deployments
- Citation-backed answer generation
- Query IDs for traceability
- Retriever version metadata in every response
- Grounding signal based on retrieved evidence
- Query latency measurement
- JSONL query trace stream for local observability
- FastAPI `/answer` API
- CLI workflows for demos and queries
- Runtime configuration through environment variables
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record

## Quickstart

```bash
pip install .[dev]
ragctl demo
uvicorn enterprise_rag.api:app --reload
pytest -q
```

## API

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/answer \
  -H 'Content-Type: application/json' \
  -d @sample_query.json
```

## Docker

```bash
docker-compose up --build
```

## Runtime Configuration

See `.env.example` for environment, retriever version, chunk size, grounding threshold, and query trace settings.

## Documentation

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `docs/adr-001-rag-service-layer.md`
- `sample_query.json`

## Production Roadmap

- Vector database support
- Hybrid dense and sparse retrieval
- Tenant-aware document permissions
- LLM answer synthesis with guardrails
- Retrieval evaluation dashboards
- Source refresh jobs and ingestion workers
