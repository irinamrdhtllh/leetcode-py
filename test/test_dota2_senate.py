from src.dota2_senate import predictPartyVictory


def test_case_1():
    senate = "RDD"
    actual = predictPartyVictory(senate)
    expected = "Dire"
    assert actual == expected


def test_case_2():
    senate = "RD"
    actual = predictPartyVictory(senate)
    expected = "Radiant"
    assert actual == expected
