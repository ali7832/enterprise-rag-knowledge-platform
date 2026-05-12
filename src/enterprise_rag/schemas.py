from __future__ import annotations

from pydantic import BaseModel


class Document(BaseModel):
    doc_id: str
    title: str
    text: str


class Chunk(BaseModel):
    chunk_id: str
    doc_id: str
    title: str
    text: str


class AnswerRequest(BaseModel):
    query: str
    top_k: int = 3


class AnswerResponse(BaseModel):
    answer: str
    citations: list[dict]
