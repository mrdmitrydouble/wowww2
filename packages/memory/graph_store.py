class GraphStore:
    """Simple adjacency list graph store."""

    def __init__(self):
        self._edges = {}

    def add_edge(self, src, dst):
        self._edges.setdefault(src, set()).add(dst)

    def neighbors(self, node):
        return list(self._edges.get(node, []))
