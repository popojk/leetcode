"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List


class ButtomUpSolution:
    """
    Time: O(N)
    Space: O(1)
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2, prev1 = 0, nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i]+prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
    
class TopDownSolution:
    """
    Time: O(N)
    Space: O(N)
    """
    def rob(self, nums: List[int]) -> int:
        memo = [None] * (len(nums) + 1)
        def dp(i: int) -> int:
            if i == 0:
                return 0
            if i == 1:
                return nums[0]
            
            if memo[i] is not None:
                return memo[i]
            memo[i] = max(nums[i-1] + dp(i-2), dp(i-1))
            return memo[i]

        return dp(len(nums))
