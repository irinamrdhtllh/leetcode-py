from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []

        def enqueue(num: int):
            queue.append(num)
            bubbleUp(len(queue) - 1)

        def dequeueMax() -> int:
            if not queue:
                return None
            queue[0], queue[-1] = queue[-1], queue[0]
            max_num = queue.pop()
            bubbleDown(0)
            return max_num

        def bubbleUp(i: int):
            root_i = (i - 1) // 2
            while i > 0 and queue[i] > queue[root_i]:
                queue[i], queue[root_i] = queue[root_i], queue[i]
                i = root_i
                root_i = (i - 1) // 2

        def bubbleDown(i: int):
            n = len(queue)
            while True:
                l = 2 * i + 1
                r = 2 * i + 2
                largest = i

                if l < n and queue[l] > queue[largest]:
                    largest = l
                if r < n and queue[r] > queue[largest]:
                    largest = r
                if largest == i:
                    break

                queue[i], queue[largest] = queue[largest], queue[i]
                i = largest

        for num in nums:
            enqueue(num)

        for _ in range(k - 1):
            dequeueMax()

        return dequeueMax()
