from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True

    len_flowerbed = len(flowerbed)
    for i in range(len_flowerbed):
        if (
            flowerbed[i] == 0
            and (i == 0 or flowerbed[i - 1] == 0)
            and (i == len_flowerbed - 1 or flowerbed[i + 1] == 0)
        ):
            flowerbed[i] = 1
            n -= 1
        if n == 0:
            return True

    return False
