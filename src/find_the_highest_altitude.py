from typing import List


def largestAltitude(gain: List[int]) -> int:
    altitudes = [0]
    for i in range(len(gain)):
        altitudes.append(altitudes[i] + gain[i])
    return max(altitudes)
