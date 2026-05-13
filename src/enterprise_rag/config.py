from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class RagSettings:
    environment: str = os.getenv('RAG_ENV', 'local')
    service_name: str = os.getenv('RAG_SERVICE_NAME', 'enterprise-rag-knowledge-platform')
    retriever_version: str = os.getenv('RAG_RETRIEVER_VERSION', 'tfidf-baseline-v1')
    default_top_k: int = int(os.getenv('RAG_DEFAULT_TOP_K', '3'))
    chunk_size: int = int(os.getenv('RAG_CHUNK_SIZE', '80'))
    minimum_relevance_score: float = float(os.getenv('RAG_MINIMUM_RELEVANCE_SCORE', '0.05'))
    trace_store_path: str = os.getenv('RAG_TRACE_STORE_PATH', 'rag_queries.jsonl')


settings = RagSettings()
