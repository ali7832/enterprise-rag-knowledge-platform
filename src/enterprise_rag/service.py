from __future__ import annotations

import time
from uuid import uuid4

from enterprise_rag.answering import AnswerEngine
from enterprise_rag.chunking import chunk_document
from enterprise_rag.config import settings
from enterprise_rag.sample_data import sample_documents
from enterprise_rag.schemas import AnswerRequest, AnswerResponse, Citation, HealthResponse
from enterprise_rag.tracing import append_query_trace


class RagKnowledgeService:
    def __init__(self) -> None:
        self.chunks = []
        for document in sample_documents():
            self.chunks.extend(chunk_document(document, chunk_size=settings.chunk_size))
        self.engine = AnswerEngine(self.chunks)

    def health(self) -> HealthResponse:
        return HealthResponse(
            status='ok',
            service_name=settings.service_name,
            environment=settings.environment,
            retriever_version=settings.retriever_version,
            indexed_chunks=len(self.chunks),
        )

    def answer(self, request: AnswerRequest) -> AnswerResponse:
        started = time.perf_counter()
        query_id = str(uuid4())
        raw_response = self.engine.answer(request.query, top_k=request.top_k)
        citations = [Citation(**item) if isinstance(item, dict) else item for item in raw_response.citations]
        grounded = bool(citations) and any(item.score >= settings.minimum_relevance_score for item in citations)
        latency_ms = round((time.perf_counter() - started) * 1000, 2)

        response = AnswerResponse(
            query_id=query_id,
            answer=raw_response.answer,
            citations=citations,
            retriever_version=settings.retriever_version,
            grounded=grounded,
            latency_ms=latency_ms,
        )
        append_query_trace(
            {
                'query_id': query_id,
                'query': request.query,
                'user_id': request.user_id,
                'session_id': request.session_id,
                'grounded': grounded,
                'latency_ms': latency_ms,
                'citation_count': len(citations),
            },
            settings.trace_store_path,
        )
        return response
