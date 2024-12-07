from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    n_row = len(grid)
    n_col = len(grid[0])
    visited = {}
    surroundings = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_area = 0
    area = 0

    def visit(u):
        visited[u] = True
        nonlocal area
        area += 1
        x, y = u
        for s in surroundings:
            xx = x + s[0]
            yy = y + s[1]
            if xx >= 0 and xx < n_col and yy >= 0 and yy < n_row:
                v = (xx, yy)
                if not visited.get(v, False) and grid[yy][xx] == 1:
                    visit(v)

    for y in range(n_row):
        for x in range(n_col):
            u = (x, y)
            if not visited.get(u, False) and grid[y][x] == 1:
                area = 0
                visit(u)
                max_area = max(max_area, area)

    return max_area
