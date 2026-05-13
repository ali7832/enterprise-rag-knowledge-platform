from fastapi import FastAPI

from enterprise_rag.schemas import AnswerRequest, AnswerResponse, HealthResponse
from enterprise_rag.service import RagKnowledgeService

app = FastAPI(title='Enterprise RAG Knowledge Platform', version='0.2.0')

_service = RagKnowledgeService()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return _service.health()


@app.post('/answer', response_model=AnswerResponse)
def answer(request: AnswerRequest) -> AnswerResponse:
    return _service.answer(request)
