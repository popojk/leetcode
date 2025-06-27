"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(N log K)
        Space: O(N)
        """
        # init a hash map to store number: count k-v pair
        hash_map = Counter(nums)
        # init a min heap to store result, each element like (count, number)
        min_heap = []
        # iterate the map k, v pair
        for number, count in hash_map.items():
            # push (count, number) into the min_heap
            heapq.heappush(min_heap, (count, number))
            # if the len(min_heap) > k, do heappop
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        # return the number in min_heap as list
        return [number for _, number in min_heap]

class BucketSortSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(N)
        Space: O(N)
        """
        hash_map = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        # init hash map
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        # init bucket
        for number, count in hash_map.items():
            bucket[count].append(number)
        # iterate bucket from the end until len(res) == k
        res = []
        for i in range(len(bucket)-1, -1, -1):
            numbers = bucket[i]
            for num in numbers:
                res.append(num)
                if len(res) == k:
                    return res