from src.evaluate_division import Solution


solution = Solution()


def test_case_1():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    actual = solution.calcEquation(equations, values, queries)
    expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    assert actual == expected


def test_case_2():
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    actual = solution.calcEquation(equations, values, queries)
    expected = [3.75000, 0.40000, 5.00000, 0.20000]
    assert actual == expected


def test_case_3():
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    actual = solution.calcEquation(equations, values, queries)
    expected = [0.50000, 2.00000, -1.00000, -1.00000]
    assert actual == expected
