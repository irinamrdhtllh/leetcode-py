from src.maximum_average_subarray_1 import findMaxAverage


def test_case_1():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    actual = findMaxAverage(nums, k)
    expected = 12.75000
    assert actual == expected


def test_case_2():
    nums = [5]
    k = 1
    actual = findMaxAverage(nums, k)
    expected = 5.00000
    assert actual == expected
