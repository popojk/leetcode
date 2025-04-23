"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time: O(N ^ 2)
        Space: O(N)
        """
        # make a dp list with len(nums) and init with 1
        # each dp will store maximum increasing len to that idx
        dp = [1] * len(nums)
        # iterate nums, if nums[i] > nums[j], compare dp[i] and dp[j+1] and store the bigger one in dp[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        # the answer will be max(dp)
        return max(dp)
