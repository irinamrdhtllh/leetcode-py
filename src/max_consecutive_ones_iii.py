from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    i = 0
    zeros = 0
    max_consecutive = 0

    for j in range(len(nums)):
        if nums[j] == 0:
            zeros += 1
        while zeros > k:
            if nums[i] == 0:
                zeros -= 1
            i += 1
        max_consecutive = max(max_consecutive, j - i + 1)

    return max_consecutive
