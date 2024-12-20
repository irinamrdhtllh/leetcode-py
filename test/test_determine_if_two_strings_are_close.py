from src.determine_if_two_strings_are_close import closeStrings


def test_case_1():
    word1 = "abc"
    word2 = "bca"
    actual = closeStrings(word1, word2)
    expected = True
    assert actual == expected


def test_case_2():
    word1 = "a"
    word2 = "aa"
    actual = closeStrings(word1, word2)
    expected = False
    assert actual == expected


def test_case_3():
    word1 = "cabbba"
    word2 = "abbccc"
    actual = closeStrings(word1, word2)
    expected = True
    assert actual == expected
