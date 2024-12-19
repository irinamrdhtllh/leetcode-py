from src.increasing_triplet_subsequence import increasingTriplet


def test_case_1():
    nums = [1, 2, 3, 4, 5]
    actual = increasingTriplet(nums)
    expected = True
    assert actual == expected


def test_case_2():
    nums = [5, 4, 3, 2, 1]
    actual = increasingTriplet(nums)
    expected = False
    assert actual == expected


def test_case_3():
    nums = [2, 1, 5, 0, 4, 6]
    actual = increasingTriplet(nums)
    expected = True
    assert actual == expected
