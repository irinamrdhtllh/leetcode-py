from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid = grid
        n_row = len(grid)
        n_col = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        queue = []
        cell_to_visit = 0
        for i in range(n_row):
            for j in range(n_col):
                u = (i, j)
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    cell_to_visit += 1

        total_mins = 0
        while queue:
            curr_row, curr_col, curr_mins = queue.pop(0)

            total_mins = max(total_mins, curr_mins)

            for drow, dcol in directions:
                next_row = curr_row + drow
                next_col = curr_col + dcol
                if 0 <= next_row < n_row and 0 <= next_col < n_col:
                    if grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        cell_to_visit -= 1
                        queue.append((next_row, next_col, curr_mins + 1))

        if cell_to_visit > 0:
            return -1

        return total_mins
