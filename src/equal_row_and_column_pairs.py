from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    rows = {}
    pairs = 0
    n = len(grid)

    for i in range(n):
        r = grid[i]
        if str(r) in rows.keys():
            rows[str(r)] += 1
        else:
            rows[str(r)] = 1

    for j in range(n):
        c = [r[j] for r in grid]
        if str(c) in rows.keys():
            pairs += rows[str(c)]

    return pairs
