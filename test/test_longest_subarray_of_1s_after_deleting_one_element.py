from src.longest_subarray_of_1s_after_deleting_one_element import longestSubarray


def test_case_1():
    nums = [1, 1, 0, 1]
    actual = longestSubarray(nums)
    expected = 3
    assert actual == expected


def test_case_2():
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    actual = longestSubarray(nums)
    expected = 5
    assert actual == expected


def test_case_3():
    nums = [1, 1, 1]
    actual = longestSubarray(nums)
    expected = 2
    assert actual == expected
