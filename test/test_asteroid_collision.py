from src.asteroid_collision import asteroidCollision


def test_case_1():
    asteroids = [5, 10, -5]
    actual = asteroidCollision(asteroids)
    expected = [5, 10]
    assert actual == expected


def test_case_2():
    asteroids = [8, -8]
    actual = asteroidCollision(asteroids)
    expected = []
    assert actual == expected


def test_case_3():
    asteroids = [10, 2, -5]
    actual = asteroidCollision(asteroids)
    expected = [10]
    assert actual == expected
