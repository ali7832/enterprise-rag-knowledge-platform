# Enterprise RAG Knowledge Platform

Production-ready retrieval-augmented generation platform for enterprise knowledge search, citation-backed answers, document ingestion, and API-based retrieval workflows.

## Features

- Document ingestion and chunking pipeline
- Metadata-aware chunk schema
- TF-IDF retrieval baseline
- Citation-backed answer generation
- FastAPI answer API
- CLI workflows for asking questions and demos
- Local JSON knowledge store
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest test suite
- Architecture and deployment documentation

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

## Docs

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `sample_query.json`

## Portfolio Highlights

- Enterprise-style RAG architecture
- Retrieval, citations, APIs, CLI, Docker, and CI
- Clear foundation for vector databases, LLM orchestration, hybrid retrieval, permissions, and production knowledge systems
