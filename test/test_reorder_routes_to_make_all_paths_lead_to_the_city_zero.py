from src.reorder_routes_to_make_all_paths_lead_to_the_city_zero import Solution


solution = Solution()


def test_case_1():
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    actual = solution.minReorder(n, connections)
    expected = 3
    assert actual == expected


def test_case_2():
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    actual = solution.minReorder(n, connections)
    expected = 2
    assert actual == expected


def test_case_3():
    n = 3
    connections = [[1, 0], [2, 0]]
    actual = solution.minReorder(n, connections)
    expected = 0
    assert actual == expected
