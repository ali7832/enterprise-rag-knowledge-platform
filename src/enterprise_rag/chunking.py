from __future__ import annotations

from enterprise_rag.schemas import Chunk, Document


def chunk_document(document: Document, chunk_size: int = 500) -> list[Chunk]:
    words = document.text.split()
    chunks: list[Chunk] = []

    for index in range(0, len(words), chunk_size):
        text = ' '.join(words[index:index + chunk_size])
        chunks.append(
            Chunk(
                chunk_id=f'{document.doc_id}-{len(chunks)}',
                doc_id=document.doc_id,
                title=document.title,
                text=text,
            )
        )

    return chunks
