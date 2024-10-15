from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """時間複雜度O(n log n)，空間複雜度O(n)"""
        merged = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval

        merged.append(prev)
        return merged
