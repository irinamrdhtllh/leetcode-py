from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row_in, col_in = entrance
        n_row, n_col = len(maze), len(maze[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        visited = {(row_in, col_in): True}
        queue = [(row_in, col_in, 0)]

        while queue:
            row, col, step = queue.pop(0)

            # Check if it is an exit
            if row != row_in or col != col_in:
                if row == 0 or col == 0 or row == n_row - 1 or col == n_col - 1:
                    return step

            # Traverse surroundings
            for drow, dcol in directions:
                next_row, next_col = row + drow, col + dcol
                if 0 <= next_row < n_row and 0 <= next_col < n_col:
                    if maze[next_row][next_col] == "." and not visited.get(
                        (next_row, next_col), False
                    ):
                        visited[(next_row, next_col)] = True
                        queue.append((next_row, next_col, step + 1))

        return -1
