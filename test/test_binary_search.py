from src.binary_search import search


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    actual = search(nums, target)
    expected = 4
    assert actual == expected


def test_case_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    actual = search(nums, target)
    expected = -1
    assert actual == expected


def test_case_3():
    nums = [3]
    target = 3
    actual = search(nums, target)
    expected = 0
    assert actual == expected
