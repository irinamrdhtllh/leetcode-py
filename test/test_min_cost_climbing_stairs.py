from src.min_cost_climbing_stairs import minCostClimbingStairs


def test_case_1():
    cost = [10, 15, 20]
    actual = minCostClimbingStairs(cost)
    expected = 15
    assert actual == expected


def test_case_2():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    actual = minCostClimbingStairs(cost)
    expected = 6
    assert actual == expected
