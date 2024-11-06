from src.contains_duplicate import containsDuplicate


def test_case_1():
    nums = [1, 2, 3, 1]
    actual = containsDuplicate(nums)
    expected = True
    assert actual == expected

def test_case_2():
    nums = [1, 2, 3, 4]
    actual = containsDuplicate(nums)
    expected = False
    assert actual == expected

def test_case_3():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    actual = containsDuplicate(nums)
    expected = True
    assert actual == expected