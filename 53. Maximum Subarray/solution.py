from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        max_sum = nums[0]
        for i in range(1, nums):
            dp.append(max(dp[i-1]+nums[i], nums[i]))
            max_sum = max(max_sum, dp[i])
        return max_sum
