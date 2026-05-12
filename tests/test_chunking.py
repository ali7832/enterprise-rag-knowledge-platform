from enterprise_rag.chunking import chunk_document
from enterprise_rag.schemas import Document


def test_chunk_document_creates_chunks():
    document = Document(doc_id='doc1', title='Test', text='one two three four five')
    chunks = chunk_document(document, chunk_size=2)

    assert len(chunks) == 3
    assert chunks[0].doc_id == 'doc1'
    assert chunks[0].title == 'Test'
