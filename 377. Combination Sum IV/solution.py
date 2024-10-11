from typing import List


class DPButtomUpSolution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [[0, False] for _ in range(target+1)]
        dp[0] = [1, True]
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0 and dp[i-num][1]:
                    dp[i][0] += dp[i-num][0]
                    dp[i][1] = True
        return dp[-1][0]
