from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    result = []
    for i in range(len(candies)):
        current = candies[i]
        current += extraCandies
        if current >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result
