from typing import List


def pivotIndex(nums: List[int]) -> int:
    i = 0
    left_sum = 0
    right_sum = sum(nums[i + 1 : len(nums)])
    while i < len(nums):
        if left_sum == right_sum:
            return i
        if i > 0:
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        i += 1
    return -1
