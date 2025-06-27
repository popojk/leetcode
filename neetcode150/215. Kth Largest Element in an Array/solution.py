"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

"""
nums: [1, 2, 3, 4] k=2 res=3
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time: O(N log K)
        Space: O(K)
        """
        # make a heap to store heapify list
        heap = []
        # iterate nums
        for num in nums:
            # push num into heap
            heapq.heappush(heap, num)
            # pop out addition element from heap to keep the size of it
            while len(heap) > k:
                heapq.heappop(heap)
        # return the value of heappop
        return heapq.heappop(heap)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([1, 2, 2, 3, 4, 5], 5)) # expected output: 2
    print(solution.findKthLargest([1], 1)) # expected output: 1