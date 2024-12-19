from src.container_with_most_water import maxArea


def test_case_1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    actual = maxArea(height)
    expected = 49
    assert actual == expected


def test_case_2():
    height = [1, 1]
    actual = maxArea(height)
    expected = 1
    assert actual == expected
