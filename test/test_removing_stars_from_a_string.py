from src.removing_stars_from_a_string import removeStars


def test_case_1():
    s = "leet**cod*e"
    actual = removeStars(s)
    expected = "lecoe"
    assert actual == expected


def test_case_2():
    s = "erase*****"
    actual = removeStars(s)
    expected = ""
    assert actual == expected
