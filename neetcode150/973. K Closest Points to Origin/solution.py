"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time: O(N log K)
        Space: O(K)
        """
        # init a min_heap to store element in format (distance, point)
        min_heap = []
        #  impelement a get_distence function to find disance
        def get_distance(x: int, y: int) -> int:
            return (x * x) + (y * y)
        # run for loop to iterate points
        for x, y in points:
            # calculate distance
            distance = get_distance(x, y)
            # push result in min_heap
            heapq.heappush(min_heap, (-distance, (x, y)))
            # if len(min_heap) > k, do heappop
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # append points in heap to result list
        res = [point for _, point in min_heap]
        return res
    
    

