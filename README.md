# Enterprise RAG Knowledge Platform

Production-ready retrieval-augmented generation platform for enterprise knowledge search, citation-backed answers, document ingestion, and API-based retrieval workflows.

## Features

- Document ingestion pipeline
- Text chunking and metadata tracking
- TF-IDF based retrieval baseline
- Citation-backed answer generation
- FastAPI search and answer API
- CLI workflows for ingest/search/demo
- Local JSON knowledge store
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest test suite

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

## Portfolio Highlights

- Enterprise-style RAG architecture
- Retrieval, citations, APIs, CLI, Docker, and CI
- Strong foundation for vector databases, LLM orchestration, and production knowledge systems
