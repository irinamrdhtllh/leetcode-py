from src.can_place_flowers import canPlaceFlowers


def test_case_1():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    actual = canPlaceFlowers(flowerbed, n)
    expected = True
    assert actual == expected


def test_case_2():
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    actual = canPlaceFlowers(flowerbed, n)
    expected = False
    assert actual == expected


def test_case_3():
    flowerbed = [1, 0, 0, 0, 0, 1, 0]
    n = 2
    actual = canPlaceFlowers(flowerbed, n)
    expected = False
    assert actual == expected
