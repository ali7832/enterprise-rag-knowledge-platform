# ADR-001: RAG Service Layer and Query Traceability

## Status

Accepted

## Context

Enterprise knowledge systems need more than retrieval results. Teams need query IDs, retriever versioning, grounding signals, latency metadata, and traceability for evaluation and operations.

## Decision

Introduce a `RagKnowledgeService` that owns indexing, retrieval execution, answer generation, grounding checks, health metadata, and query tracing.

## Consequences

Benefits:

- FastAPI routes remain thin and easy to deploy.
- Every answer has a query ID and retriever version.
- Query traces can be reviewed for debugging and evaluation.
- Health checks expose indexed chunk count and deployment metadata.

Tradeoffs:

- Local JSONL tracing is suitable for demos, but production systems should use a database or observability backend.
- TF-IDF retrieval is explainable and lightweight, but production systems should add embeddings and hybrid retrieval.
