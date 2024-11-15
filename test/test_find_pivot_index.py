from src.find_pivot_index import pivotIndex


def test_case_1():
    nums = [1, 7, 3, 6, 5, 6]
    actual = pivotIndex(nums)
    expected = 3
    assert actual == expected


def test_case_2():
    nums = [1, 2, 3]
    actual = pivotIndex(nums)
    expected = -1
    assert actual == expected


def test_case_3():
    nums = [2, 1, -1]
    actual = pivotIndex(nums)
    expected = 0
    assert actual == expected
