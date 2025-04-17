"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class ButtomUpSolution:
    def climbStairs(self, n: int) -> int:
        """
        Time: O(N)
        Space: O(N)
        """
        if n == 1:
            return 1
        elif n == 2:
            return 3
        dp = 0 * (n+1)
        dp[1] = 1
        dp[2] = 3
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
class TopDownSolution:
    def climbStairs(self, n: int) -> int:
        """
        Time: O(N)
        Space: O(N)
        """
        memo = {}
        def dfs(n: int) -> int:
            if n == 0 or n == 1:
                memo[1]=1
                return 1
            memo[n] = memo[n] if n in memo else dfs(n-1) + dfs(n-2)
            return memo[n]
        return dfs(n)
