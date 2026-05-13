from enterprise_rag.schemas import AnswerRequest
from enterprise_rag.service import RagKnowledgeService


def test_rag_service_returns_query_metadata_and_citations():
    service = RagKnowledgeService()
    response = service.answer(
        AnswerRequest(
            query='What security controls are required for enterprise systems?',
            user_id='user_001',
            session_id='session_001',
        )
    )

    assert response.query_id
    assert response.retriever_version
    assert response.latency_ms >= 0
    assert response.citations
    assert response.grounded is True


def test_rag_service_health_contains_index_metadata():
    service = RagKnowledgeService()
    health = service.health()

    assert health.status == 'ok'
    assert health.indexed_chunks > 0
    assert health.retriever_version
