from src.rotting_oranges import Solution


solution = Solution()


def test_case_1():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    actual = solution.orangesRotting(grid)
    expected = 4
    assert actual == expected


def test_case_2():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    actual = solution.orangesRotting(grid)
    expected = -1
    assert actual == expected


def test_case_3():
    grid = [[0, 2]]
    actual = solution.orangesRotting(grid)
    expected = 0
    assert actual == expected
