"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n⋅n!)
        Space: O(n⋅n!)
        """
        # declare a res list to store answer
        res = []
        # impelement a backtrack method accept a path, nums input
        def backtrack(path: List, nums: List) -> None:
            # backtrack should stop when nums is empty and append path
            if not nums:
                res.append(path)
                return
            # for every element in nums, append it in path
            # pass path and nums without element to the next permute
            for i in range(len(nums)):
                backtrack(path + [nums[i]], nums[:i]+nums[i+1:])
        backtrack([], nums)
        return res
                
