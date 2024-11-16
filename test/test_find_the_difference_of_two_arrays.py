from src.find_the_difference_of_two_arrays import findDifference


def test_case_1():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    actual = findDifference(nums1, nums2)
    expected = [[1, 3], [4, 6]]
    assert actual == expected


def test_case_2():
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    actual = findDifference(nums1, nums2)
    expected = [[3], []]
    assert actual == expected
