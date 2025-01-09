from src.number_of_provinces import Solution


solution = Solution()


def test_case_1():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    actual = solution.findCircleNum(isConnected)
    expected = 2
    assert actual == expected


def test_case_2():
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    actual = solution.findCircleNum(isConnected)
    expected = 3
    assert actual == expected
