from typing import List


def countBits(n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = bin(i)[2:].count("1")
    return ans
