from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    i_th = float("inf")
    j_th = float("inf")

    for num in nums:
        if num <= i_th:
            i_th = num
        elif num <= j_th:
            j_th = num
        else:
            return True

    return False
