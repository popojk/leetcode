from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """時間複雜度O(n log n)，空間複雜度O(n)"""
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        count = 0

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                count += 1
            else:
                prev = interval
        return count
