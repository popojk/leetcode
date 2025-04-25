"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] 

(start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.
"""

from typing import List

"""
hint: find the number of non overlaping sets of intervals
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Time: O(Nlog N) which is given by the sorting process
        Space: O(N)
        """
        # store sorted start time and end time in 2 different arrays
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        # init variable start_idx and end_idx to record iterate position
        start_idx, end_idx = 0, 0
        # init res, count to store final answer and current count while iterating
        res, count = 0, 0
        # run a while loop when start_idx < len(start)
        while start_idx < len(intervals):
            # if start[start_idx] < end(end_idx), increase count by 1 as there is overlaping intervals and start_idx += 1
            if start[start_idx] < end[end_idx]:
                start_idx += 1
                count += 1
            # in other cases, count -= 1 and end_idx += 1 as there is an interval is over
            else:
                end_idx += 1
                count -= 1
            # take the max of (res, count) in each iteration
            res = max(res, count)
        # return res as answer
        return res
