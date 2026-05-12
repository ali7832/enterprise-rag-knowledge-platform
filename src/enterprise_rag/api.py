from fastapi import FastAPI

from enterprise_rag.answering import AnswerEngine
from enterprise_rag.chunking import chunk_document
from enterprise_rag.sample_data import sample_documents
from enterprise_rag.schemas import AnswerRequest, AnswerResponse

app = FastAPI(title='Enterprise RAG Knowledge Platform')

_chunks = []
for document in sample_documents():
    _chunks.extend(chunk_document(document, chunk_size=80))

_engine = AnswerEngine(_chunks)


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/answer', response_model=AnswerResponse)
def answer(request: AnswerRequest) -> AnswerResponse:
    return _engine.answer(request.query, top_k=request.top_k)
