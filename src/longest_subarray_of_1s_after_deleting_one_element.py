from typing import List


def longestSubarray(nums: List[int]) -> int:
    i = 0
    deleted = 0
    longest = 0

    for j in range(len(nums)):
        if nums[j] == 0:
            deleted += 1

        while deleted > 1:
            if nums[i] == 0:
                deleted -= 1
            i += 1

        longest = max(longest, j - i)

    return longest
