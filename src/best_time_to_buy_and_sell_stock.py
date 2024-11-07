from typing import List


def maxProfit(prices: List[int]) -> int:
    left = 0
    right = 0
    max_profit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit < 0:
            left += 1
        elif profit >= 0:
            right += 1
        if profit > max_profit:
            max_profit = profit
    return max_profit
