from src.max_consecutive_ones_iii import longestOnes


def test_case_1():
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    actual = longestOnes(nums, k)
    expected = 6
    assert actual == expected


def test_case_2():
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    actual = longestOnes(nums, k)
    expected = 10
    assert actual == expected
