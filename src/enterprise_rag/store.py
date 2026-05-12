from __future__ import annotations

import json
from pathlib import Path

from enterprise_rag.schemas import Chunk


class KnowledgeStore:
    def __init__(self, path: str | Path = 'knowledge_store.json') -> None:
        self.path = Path(path)

    def save(self, chunks: list[Chunk]) -> None:
        payload = [chunk.model_dump() for chunk in chunks]
        self.path.write_text(json.dumps(payload, indent=2), encoding='utf-8')

    def load(self) -> list[Chunk]:
        if not self.path.exists():
            return []
        payload = json.loads(self.path.read_text(encoding='utf-8'))
        return [Chunk(**item) for item in payload]
