import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        time: O(n log k)
        space: O(k)
        """
        heap = []
        count = 0

        for num in nums:
            heapq.heappush(heap, num)
            count += 1
            if count > k:
                heapq.heappop(heap)
                count -= 1
        return heap[0]
