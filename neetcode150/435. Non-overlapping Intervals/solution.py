"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 

return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Time: O(N log N)
        Space: O(N)
        """
        # init a res to count overlaping intervals
        res = 0
        if len(intervals) == 1:
            return res
        # sort the intervals based on the end point of each element in asc order
        intervals.sort(key=lambda x: x[1])
        # init a var called prev_end to store the end idx of previous element
        prev_end = intervals[0][1]
        # iterate intervals from second element, which i == 1
        for i in range(1, len(intervals)):
            # if curr start < prev_end, res += 1
            if intervals[i][0] < prev_end:
                res += 1
            else:
                # we only update prev_end if intervals are not overlaping
                prev_end = intervals[i][1]
        return res