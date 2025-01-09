from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # Build the graph (includes reverse edges)
        self.graph = {}
        for i, (u, v) in enumerate(equations):
            if u not in self.graph.keys():
                self.graph[u] = []
            self.graph[u].append((v, values[i]))
            if v not in self.graph.keys():
                self.graph[v] = []
            self.graph[v].append((u, 1 / values[i]))

        queries_values = []
        for a, b in queries:
            if a not in self.graph.keys() or b not in self.graph.keys():
                queries_values.append(-1)
            else:
                self.visited = {}
                queries_values.append(self.DFSVisit(a, b, 1))

        return queries_values

    def DFSVisit(self, u: int, goal: int, value: float) -> float:
        self.visited[u] = True

        if u == goal:
            return value

        for v, w in self.graph[u]:
            if not self.visited.get(v, False):
                result = self.DFSVisit(v, goal, value * w)
                if result != -1:
                    return result

        return -1
