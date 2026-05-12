from enterprise_rag.answering import AnswerEngine
from enterprise_rag.chunking import chunk_document
from enterprise_rag.schemas import Document


def test_answer_engine_returns_citations():
    document = Document(
        doc_id='security',
        title='Security Policy',
        text='Enterprise systems require multi factor authentication and audit logging.',
    )
    engine = AnswerEngine(chunk_document(document, chunk_size=20))
    response = engine.answer('What security controls are required?')

    assert response.citations
    assert 'retrieved enterprise knowledge' in response.answer
