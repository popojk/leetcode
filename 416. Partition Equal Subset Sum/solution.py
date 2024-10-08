from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odd, return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = [True] + [False]*s
        for num in nums:
            for curr in range(s, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
        return dp[s//2]
