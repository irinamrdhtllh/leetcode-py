from src.product_of_array_except_self import productExceptSelf


def test_case_1():
    nums = [1, 2, 3, 4]
    actual = productExceptSelf(nums)
    expected = [24, 12, 8, 6]
    assert actual == expected


def test_case_2():
    nums = [-1, 1, 0, -3, 3]
    actual = productExceptSelf(nums)
    expected = [0, 0, 9, 0, 0]
    assert actual == expected
