from src.valid_anagram import isAnagram


def test_case_1():
    s = "anagram"
    t = "nagaram"
    actual = isAnagram(s, t)
    expected = True
    assert actual == expected


def test_case_2():
    s = "rat"
    t = "car"
    actual = isAnagram(s, t)
    expected = False
    assert actual == expected


def test_case_3():
    s = "aacc"
    t = "ccac"
    actual = isAnagram(s, t)
    expected = False
    assert actual == expected
