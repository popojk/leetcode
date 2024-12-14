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


class OptimizeSolution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odd, return False
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = [True] + [False]*(s >> 1)
        for num in nums:
            for curr in range(s >> 1, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
        return dp[-1]


class SecondOptimizeSolution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odd, return False
        dp, s = set([0]), sum(nums)
        if s % 2 != 0:
            return False
        for num in nums:
            for curr in range(s >> 1, num-1, -1):
                if curr not in dp and curr-num in dp:
                    if curr == s >> 1:
                        return True
                    dp.add(curr)
        return False
