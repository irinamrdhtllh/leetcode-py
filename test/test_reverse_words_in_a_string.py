from src.reverse_words_in_a_string import reverseWords


def test_case_1():
    s = "the sky is blue"
    actual = reverseWords(s)
    expected = "blue is sky the"
    assert actual == expected


def test_case_2():
    s = "  hello world  "
    actual = reverseWords(s)
    expected = "world hello"
    assert actual == expected


def test_case_3():
    s = "a good   example"
    actual = reverseWords(s)
    expected = "example good a"
    assert actual == expected
