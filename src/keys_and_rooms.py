from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.rooms = rooms
        self.n_rooms = len(rooms)
        self.visited = {}

        self.DFSVisit(0)

        for key in range(self.n_rooms):
            if not self.visited.get(key, False):
                return False

        return True

    def DFSVisit(self, u):
        self.visited[u] = True
        for v in self.rooms[u]:
            if not self.visited.get(v, False):
                self.DFSVisit(v)
