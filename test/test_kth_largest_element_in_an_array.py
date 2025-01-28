from src.kth_largest_element_in_an_array import Solution


solution = Solution()


def test_case_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    actual = solution.findKthLargest(nums, k)
    expected = 5
    assert actual == expected


def test_case_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    actual = solution.findKthLargest(nums, k)
    expected = 4
    assert actual == expected
