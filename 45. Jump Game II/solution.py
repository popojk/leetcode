from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0
        while far < len(nums)-1:
            farest = 0
            for i in range(near, far+1):
                farest = max(farest, i+nums[i])
            near = far+1
            far = farest
            jumps += 1
        return jumps


class DPSolution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        dp = [0] * n
        j = 0
        for i in range(1, n):
            while j + nums[j] < i:
                j += 1
            dp[i] = dp[j] + 1
        return dp[-1]
