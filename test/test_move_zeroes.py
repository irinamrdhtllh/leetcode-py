from src.move_zeroes import moveZeroes


def test_case_1():
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    expected = [1, 3, 12, 0, 0]
    assert nums == expected


def test_case_2():
    nums = [0]
    moveZeroes(nums)
    expected = [0]
    assert nums == expected


def test_case_3():
    nums = [0, 1, 5, 0, 2, 0]
    moveZeroes(nums)
    expected = [1, 5, 2, 0, 0, 0]
    assert nums == expected
