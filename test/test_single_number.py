from src.single_number import singleNumber


def test_case_1():
    nums = [2, 2, 1]
    actual = singleNumber(nums)
    expected = 1
    assert actual == expected


def test_case_2():
    nums = [4, 1, 2, 1, 2]
    actual = singleNumber(nums)
    expected = 4
    assert actual == expected


def test_case_3():
    nums = [1]
    actual = singleNumber(nums)
    expected = 1
    assert actual == expected
