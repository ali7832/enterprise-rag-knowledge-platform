# Enterprise RAG Knowledge Platform

Deployable enterprise knowledge service for retrieval-augmented answering, metadata-aware citations, query traceability, grounding checks, API-based knowledge access, and a premium multi-page React knowledge operations dashboard.

## Product Demo Video


https://github.com/user-attachments/assets/09ffc4db-404d-4719-ac88-216ed9b0b5c7


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
- Multi-page React/Vite enterprise RAG frontend

## Quickstart

```bash
pip install .[dev]
ragctl demo
uvicorn enterprise_rag.api:app --reload
pytest -q
```

## Frontend KnowledgeCore AI Dashboard

The `frontend/` directory contains a premium React/Vite command center for enterprise knowledge teams, AI platform engineers, and business users.

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

Frontend pages:

- Overview: indexed documents, grounded answer rate, latency, query traces, retrieval charts
- Ask Knowledge: interactive question workspace with grounded answer fallback
- Ingestion: upload, chunk, index, trace, and source health workflow view
- Citation Review: evidence table with retrieved documents and confidence scores
- Grounding Monitor: quality scorecards, grounding thresholds, and guardrail signals
- Query Traces: traceable query history with chunks, groundedness, and latency
- Admin: retriever version, chunk size, threshold, trace stream, and access controls

The UI attempts to call `/answer` and falls back to demo RAG intelligence when the backend is offline.

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
