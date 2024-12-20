from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if abs(a) == stack[-1]:
                stack.pop(-1)
                break
            elif abs(a) > stack[-1]:
                stack.pop(-1)
            else:
                break
        else:
            stack.append(a)

    return stack
