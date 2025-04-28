"""
Given an array of integers temperatures represents the daily temperatures, 

return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 

If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # init a res list with len == len(temperatures) and all element = 0
        res = [0] * len(temperatures)
        # init a stack var
        stack = []
        # make a for loop to iterate all temperatures
        for i in range(len(temperatures)):
            # while len(stack) != 0 and temperatures[i] > that of last element, count days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            # push temperatures[i] into stack with format (i, temperatures[i]), we need i to calculate days
            stack.append(i)
        # return res as answer
        return res
        
