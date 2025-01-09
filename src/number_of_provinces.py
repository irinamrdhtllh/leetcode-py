from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected = isConnected
        self.visited = {}
        self.n_provinces = 0

        for u in range(len(self.isConnected)):
            if not self.visited.get(u, False):
                self.DFSVisit(u)
                self.n_provinces += 1

        return self.n_provinces

    def DFSVisit(self, u: int):
        self.visited[u] = True
        for i, v in enumerate(self.isConnected[u]):
            if not self.visited.get(i, False) and v == 1:
                self.DFSVisit(i)
