from src.two_sum import twoSum


def test_case_1():
    nums = [2, 7, 11, 15]
    target = 9
    actual = twoSum(nums, target)
    expected = [0, 1]
    assert actual == expected

def test_case_2():
    nums = [3, 2, 4]
    target = 6
    actual = twoSum(nums, target)
    expected = [1, 2]
    assert actual == expected

def test_case_3():
    nums = [3, 3]
    target = 6
    actual = twoSum(nums, target)
    expected = [0, 1]
    assert actual == expected