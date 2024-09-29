from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for __ in range(m)]
        count = 0

        def dfs(row, col):
            if row < 0 or row > m-1 or col < 0 or col > n-1 or visited[row][col] or grid[row][col] == '0':
                return
            visited[row][col] = True
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i, j)
        return count


class SpaceOptimizeSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] == '0'
                    self.helper(grid, i, j)
                    count += 1
        return count

    def helper(self, grid, i, j):
        queue = deque([(i, j)])
        while queue:
            I, J = queue.popleft()
            for i, j in [I+1, J], [I-1, J], [I, J+1], [I, J-1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))
