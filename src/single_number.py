from typing import List


def singleNumber(nums: List[int]) -> int:
    hash_map = {}
    for num in nums:
        if num in hash_map.keys():
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    for num in hash_map.keys():
        if hash_map[num] == 1:
            return num
