from __future__ import annotations

from enterprise_rag.retrieval import Retriever
from enterprise_rag.schemas import AnswerResponse, Chunk


class AnswerEngine:
    def __init__(self, chunks: list[Chunk]) -> None:
        self.retriever = Retriever(chunks)

    def answer(self, query: str, top_k: int = 3) -> AnswerResponse:
        results = self.retriever.search(query, top_k=top_k)
        if not results:
            return AnswerResponse(answer='No relevant context found.', citations=[])

        citations = []
        snippets = []
        for result in results:
            chunk = result['chunk']
            citations.append(
                {
                    'chunk_id': chunk.chunk_id,
                    'doc_id': chunk.doc_id,
                    'title': chunk.title,
                    'score': result['score'],
                }
            )
            snippets.append(chunk.text[:220])

        answer = 'Based on the retrieved enterprise knowledge: ' + ' '.join(snippets)
        return AnswerResponse(answer=answer, citations=citations)
