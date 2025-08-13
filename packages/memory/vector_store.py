from typing import List, Tuple


class VectorStore:
    """In-memory vector store stub."""

    def __init__(self):
        self._items: List[Tuple[List[float], str]] = []

    def add(self, vector: List[float], text: str) -> None:
        self._items.append((vector, text))

    def query(self, vector: List[float]) -> List[str]:
        scored = [
            (sum(a * b for a, b in zip(v, vector)), text)
            for v, text in self._items
        ]
        scored.sort(reverse=True)
        return [text for _, text in scored]
