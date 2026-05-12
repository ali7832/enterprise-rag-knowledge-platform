from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from enterprise_rag.schemas import Chunk


class Retriever:
    def __init__(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.matrix = self.vectorizer.fit_transform([chunk.text for chunk in chunks]) if chunks else None

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        if not self.chunks or self.matrix is None:
            return []
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix)[0]
        ranked = sorted(enumerate(scores), key=lambda item: item[1], reverse=True)[:top_k]
        return [
            {
                'chunk': self.chunks[index],
                'score': round(float(score), 4),
            }
            for index, score in ranked
        ]
