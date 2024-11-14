from src.greatest_common_divisor_of_strings import gcdOfStrings


def test_case_1():
    str1 = "ABCABC"
    str2 = "ABC"
    actual = gcdOfStrings(str1, str2)
    expected = "ABC"
    assert actual == expected


def test_case_2():
    str1 = "ABABAB"
    str2 = "ABAB"
    actual = gcdOfStrings(str1, str2)
    expected = "AB"
    assert actual == expected


def test_case_3():
    str1 = "LEET"
    str2 = "CODE"
    actual = gcdOfStrings(str1, str2)
    expected = ""
    assert actual == expected
