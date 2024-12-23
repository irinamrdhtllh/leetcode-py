from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1, set2 = set(nums1), set(nums2)
    answer = [list(set1 - set2), list(set2 - set1)]
    return answer
