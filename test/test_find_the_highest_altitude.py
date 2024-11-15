from src.find_the_highest_altitude import largestAltitude


def test_case_1():
    gain = [-5, 1, 5, 0, -7]
    actual = largestAltitude(gain)
    expected = 1
    assert actual == expected


def test_case_2():
    gain = [-4, -3, -2, -1, 4, 3, 2]
    actual = largestAltitude(gain)
    expected = 0
    assert actual == expected
