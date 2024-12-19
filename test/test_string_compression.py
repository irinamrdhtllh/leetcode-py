from src.string_compression import compress


def test_case_1():
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    actual = compress(chars)
    expected = 6
    assert actual == expected


def test_case_2():
    chars = ["a"]
    actual = compress(chars)
    expected = 1
    assert actual == expected


def test_case_3():
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    actual = compress(chars)
    expected = 4
    assert actual == expected
