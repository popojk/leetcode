class ButtomUpDPSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(len(dp[0])):
            dp[0][i] = 1
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


class TopDownDPSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        return self.dfs(0, 0, m, n, memo)

    def dfs(self, x, y, m, n, memo):
        if x == m-1 and y == n-1:
            return 1

        if memo[x][y] != -1:
            return memo[x][y]

        right_paths = 0
        down_paths = 0
        if x < m-1:
            right_paths = self.dfs(x+1, y, m, n, memo)
        if y < n-1:
            down_paths = self.dfs(x, y+1, m, n, memo)
        memo[x][y] = right_paths + down_paths
        return memo[x][y]


class OptimizeSpaceSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        above_row = [1] * n
        for _ in range(m-1):
            curr_row = [1] * n
            for i in range(1, n):
                curr_row[i] = curr_row[i-1] + above_row[i]
            above_row = curr_row
        return above_row[-1]
