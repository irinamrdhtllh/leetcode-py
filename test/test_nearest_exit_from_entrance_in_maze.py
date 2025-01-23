from src.nearest_exit_from_entrance_in_maze import Solution


solution = Solution()


def test_case_1():
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    actual = solution.nearestExit(maze, entrance)
    expected = 1
    assert actual == expected


def test_case_2():
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    actual = solution.nearestExit(maze, entrance)
    expected = 2
    assert actual == expected


def test_case_3():
    maze = [[".", "+"]]
    entrance = [0, 0]
    actual = solution.nearestExit(maze, entrance)
    expected = -1
    assert actual == expected
