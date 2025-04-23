"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 

The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class ButtomUpSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(M * N)
        Space: O(M * N)
        """
        # init a n * m dp list, each element represent the unique path to that point
        dp = [[0] * n for _ in range(m)]
        # init [1, n] and [n, 1] to be 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1
        # iterate the grid
        for i in range(1, m):
            for j in range(1, n):
                # the unique path of each dp will be calculated by adding dp[i-1, j] and [i, j-1]
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # the answer will be dp[-1][-1]
        return dp[-1][-1]

class TopDownSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(M * N)
        Space: O(M * N)
        """
        memo = {}
        def dfs(m: int, n: int) -> int:
            if m == 1 or n == 1:
                return 1        
            if (m, n) in memo:
                return memo[(m, n)]          
            memo[(m, n)] = dfs(m-1, n) + dfs(m, n-1)
            return memo[(m, n)]
        return dfs(m, n)