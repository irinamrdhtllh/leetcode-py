from src.equal_row_and_column_pairs import equalPairs


def test_case_1():
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    actual = equalPairs(grid)
    expected = 1
    assert actual == expected


def test_case_2():
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    actual = equalPairs(grid)
    expected = 3
    assert actual == expected
