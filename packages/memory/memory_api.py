from .vector_store import VectorStore
from .graph_store import GraphStore


class MemoryAPI:
    """Facade over different memory backends."""

    def __init__(self):
        self.vectors = VectorStore()
        self.graph = GraphStore()

    def remember(self, vector, text, src=None, dst=None):
        self.vectors.add(vector, text)
        if src and dst:
            self.graph.add_edge(src, dst)

    def recall(self, query_vector):
        return self.vectors.query(query_vector)
