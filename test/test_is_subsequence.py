from src.is_subsequence import isSubsequence


def test_case_1():
    s = "abc"
    t = "ahbgdc"
    actual = isSubsequence(s, t)
    expected = True
    assert actual == expected


def test_case_2():
    s = "axc"
    t = "ahbgdc"
    actual = isSubsequence(s, t)
    expected = False
    assert actual == expected


def test_case_3():
    s = "aec"
    t = "abcde"
    actual = isSubsequence(s, t)
    expected = False
    assert actual == expected
