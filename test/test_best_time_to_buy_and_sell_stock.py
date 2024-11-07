from src.best_time_to_buy_and_sell_stock import maxProfit


def test_case_1():
    prices = [7, 1, 5, 3, 6, 4]
    actual = maxProfit(prices)
    expected = 5
    assert actual == expected


def test_case_2():
    prices = [7, 6, 4, 3, 1]
    actual = maxProfit(prices)
    expected = 0
    assert actual == expected


def test_case_3():
    prices = [7]
    actual = maxProfit(prices)
    expected = 0
    assert actual == expected
