from src.counting_bits import countBits


def test_case_1():
    n = 2
    actual = countBits(n)
    expected = [0, 1, 1]
    assert actual == expected


def test_case_2():
    n = 5
    actual = countBits(n)
    expected = [0, 1, 1, 2, 1, 2]
    assert actual == expected
