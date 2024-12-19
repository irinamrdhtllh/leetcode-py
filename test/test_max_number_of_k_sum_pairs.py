from src.max_number_of_k_sum_pairs import maxOperations


def test_case_1():
    nums = [1, 2, 3, 4]
    k = 5
    actual = maxOperations(nums, k)
    expected = 2
    assert actual == expected


def test_case_2():
    nums = [3, 1, 3, 4, 3]
    k = 6
    actual = maxOperations(nums, k)
    expected = 1
    assert actual == expected
