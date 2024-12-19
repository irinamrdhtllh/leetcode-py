from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # The product to the left of the number
    prods_l = [1] * len(nums)
    for i in range(1, len(nums)):
        prods_l[i] = prods_l[i - 1] * nums[i - 1]

    # The product to the right of the number
    prods_r = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        prods_r[i] = prods_r[i + 1] * nums[i + 1]

    # Combine
    prods = []
    for i in range(len(nums)):
        prods.append(prods_l[i] * prods_r[i])

    return prods
