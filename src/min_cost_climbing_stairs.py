from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    if len(cost) == 2:
        return min(cost)
    dp = [0] * (len(cost))
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[-1], dp[-2])
