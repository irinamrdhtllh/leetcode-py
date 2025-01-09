from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.connections = connections
        self.visited = {}
        self.n_change = 0

        # self.connections with reverse edges
        graph = {i: [] for i in range(n)}
        for u, v in self.connections:
            graph[u].append((v, "original"))
            graph[v].append((u, "reverse"))
        self.connections = graph

        self.DFSVisit(0)

        return self.n_change

    def DFSVisit(self, u: int):
        self.visited[u] = True
        for v, edge in self.connections[u]:
            if not self.visited.get(v, False):
                if edge == "original":
                    # The vertex is not going towards 0. We need to change the direction
                    self.n_change += 1
                self.DFSVisit(v)
