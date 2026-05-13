from __future__ import annotations

from pydantic import BaseModel, Field


class Document(BaseModel):
    doc_id: str
    title: str
    text: str
    source: str = 'internal'
    access_level: str = 'standard'


class Chunk(BaseModel):
    chunk_id: str
    doc_id: str
    title: str
    text: str
    source: str = 'internal'
    access_level: str = 'standard'


class AnswerRequest(BaseModel):
    query: str = Field(..., min_length=3)
    top_k: int = Field(default=3, ge=1, le=10)
    user_id: str | None = None
    session_id: str | None = None


class Citation(BaseModel):
    chunk_id: str
    doc_id: str
    title: str
    score: float
    source: str


class AnswerResponse(BaseModel):
    query_id: str
    answer: str
    citations: list[Citation]
    retriever_version: str
    grounded: bool
    latency_ms: float


class HealthResponse(BaseModel):
    status: str
    service_name: str
    environment: str
    retriever_version: str
    indexed_chunks: int
