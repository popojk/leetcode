"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        """
        # init left, right pointer with 0, len(height) - 1
        l, r = 0, len(height)-1
        # init a global max_area to store result
        max_area = 0
        # run while loop when l < r
        while l < r:
            # find min of height in l, r and calculate area
            curr_area = (r - l) * min(height[l], height[r])
            # update global max_area
            max_area = max(max_area, curr_area)
            # l += 1 or r -= 1 when the height is shorter
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
