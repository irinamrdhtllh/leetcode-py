from src.nth_tribonacci_number import tribonacci


def test_case_1():
    n = 4
    actual = tribonacci(n)
    expected = 4
    assert actual == expected


def test_case_2():
    n = 25
    actual = tribonacci(n)
    expected = 1389537
    assert actual == expected
