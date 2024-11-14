from src.reverse_vowels_of_a_string import reverseVowels


def test_case_1():
    s = "IceCreAm"
    actual = reverseVowels(s)
    expected = "AceCreIm"
    assert actual == expected


def test_case_2():
    s = "leetcode"
    actual = reverseVowels(s)
    expected = "leotcede"
    assert actual == expected


def test_case_3():
    s = "Euston saw I was not Sue."
    actual = reverseVowels(s)
    expected = "euston saw I was not SuE."
    assert actual == expected
