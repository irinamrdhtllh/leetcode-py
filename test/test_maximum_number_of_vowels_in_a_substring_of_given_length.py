from src.maximum_number_of_vowels_in_a_substring_of_given_length import maxVowels


def test_case_1():
    s = "abciiidef"
    k = 3
    actual = maxVowels(s, k)
    expected = 3
    assert actual == expected


def test_case_2():
    s = "aeiou"
    k = 2
    actual = maxVowels(s, k)
    expected = 2
    assert actual == expected


def test_case_3():
    s = "leetcode"
    k = 3
    actual = maxVowels(s, k)
    expected = 2
    assert actual == expected
