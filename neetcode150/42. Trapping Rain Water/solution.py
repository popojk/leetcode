"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        # make 2 pointers from pos 0, len(height)-1
        l, r = 0, len(height)-1
        # init max_left and max_right to record what it is in current position
        max_left, max_right = height[l], height[r]
        res = 0
        # make a while loop to run whenever l < r
        while l < r:
            # whenever max_left <= max_right, l+=1 and update max_left, the amount of water can trap = max_left - height[l]
            # the right doesn't matter as max_left is smaller, the water unit will be trapped regardless how high is the right side
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            # otherwise the same   
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        return res
