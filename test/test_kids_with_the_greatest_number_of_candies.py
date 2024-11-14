from src.kids_with_the_greatest_number_of_candies import kidsWithCandies


def test_case_1():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    actual = kidsWithCandies(candies, extraCandies)
    expected = [True, True, True, False, True]
    assert actual == expected


def test_case_2():
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    actual = kidsWithCandies(candies, extraCandies)
    expected = [True, False, False, False, False]
    assert actual == expected


def test_case_3():
    candies = [12, 1, 12]
    extraCandies = 10
    actual = kidsWithCandies(candies, extraCandies)
    expected = [True, False, True]
    assert actual == expected
