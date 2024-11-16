from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    hash_map = {}
    for num in arr:
        if num in hash_map.keys():
            hash_map[num] += 1
        else:
            hash_map[num] = 1
    occurrences = list(hash_map.values())
    set_occurrences = list(set(occurrences))
    return len(occurrences) == len(set_occurrences)
