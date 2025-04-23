"""
You are given an integer array nums. You are initially positioned at the array's first index, 

and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

from typing import List


class DPSolution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Time: O(N ^ 2)
        Space: O(N)
        """
        # if len nums == 1, return True
        if len(nums) == 1:
            return True
        # init a bool dp list to record whether the index can be reached
        dp = [True] + [False] * (len(nums)-1)
        # iterate nums from idx 1
        for i in range(1, len(nums)):
            # iterate j from i-1, if dp[j] == True and j+nums[j] >= i, dp[i] = True, break the for loop
            for j in range(i-1, -1, -1):
                if dp[j] and j+nums[j] >= i:
                    dp[i] = True
                    break
        # return dp[-1]
        return dp[-1]
    
class GreedySolution:
    def canJump(self, nums: List[int]) -> bool:
        # init a pos var to record current position
        pos = 0
        # init a power var to record the power to jump
        power = nums[0]
        # while current power > 0 and pos < len(nums)
        while power > 0 and pos < len(nums):
            pos += 1
            power -= 1
            power = max(power, nums[pos])
        # return if pos == len(nums)-1
        return pos == len(nums)-1