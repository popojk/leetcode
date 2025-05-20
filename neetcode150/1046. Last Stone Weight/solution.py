"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Time: O(N log N)
        Space: O(N)
        """
        # init a max_heap to store all stones(O(N log N))
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # while len(max_heap) > 0, do iterate
        while len(max_heap) > 1:
            # pop out top 2 stones, take the abs value of substracting both
            first_stone = -heapq.heappop(max_heap)
            second_stone = -heapq.heappop(max_heap)
            # push -product into max_heap if product != 0
            if first_stone != second_stone:
                heapq.heappush(max_heap, -(first_stone - second_stone))
        # stones are destroyed, return 0
        return -max_heap[0] if max_heap else 0