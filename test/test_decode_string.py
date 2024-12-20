from src.decode_string import decodeString


def test_case_1():
    s = "3[a]2[bc]"
    actual = decodeString(s)
    expected = "aaabcbc"
    assert actual == expected


def test_case_2():
    s = "3[a2[c]]"
    actual = decodeString(s)
    expected = "accaccacc"
    assert actual == expected


def test_case_3():
    s = "2[abc]3[cd]ef"
    actual = decodeString(s)
    expected = "abcabccdcdcdef"
    assert actual == expected
