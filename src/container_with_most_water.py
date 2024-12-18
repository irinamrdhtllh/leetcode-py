from typing import List


def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    max_area = 0

    while i < j:
        area = abs(i - j) * min(height[i], height[j])
        if area > max_area:
            max_area = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area
