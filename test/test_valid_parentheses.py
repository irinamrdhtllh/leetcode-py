from src.valid_parentheses import isValid


def test_case_1():
    s = "()"
    actual = isValid(s)
    expected = True
    assert actual == expected


def test_case_2():
    s = "()[]{}"
    actual = isValid(s)
    expected = True
    assert actual == expected


def test_case_3():
    s = "(]"
    actual = isValid(s)
    expected = False
    assert actual == expected


def test_case_4():
    s = "([])"
    actual = isValid(s)
    expected = True
    assert actual == expected
