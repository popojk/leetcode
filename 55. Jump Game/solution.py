from typing import List


class DPSolution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and nums[j] >= (i-j):
                    dp[i] = True
                    break
        return dp[-1]


class TopDownDPSolution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [-1] * n
        memo[0] = 1

        def can_reach(i):
            if memo[i] != -1:
                return memo[i] == 1
            for j in range(i-1, -1, -1):
                if nums[j] >= i-j and can_reach(j):
                    memo[i] = 1
                    return True
            memo[i] = 0
            return False
        return can_reach(n-1)


class GreedySolution:
    def canJump(self, nums: List[int]) -> bool:
        power = 0
        for i in range(len(nums)):
            power -= 1
            power = max(power, nums[i])

            if power == 0 and i != len(nums)-1:
                return False
        return True
