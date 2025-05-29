"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List


class Solution:

    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Time: O(M * N)
        Space: O(M * N)
        """
        # init m, n represent the llength and width 
        m, n = len(grid), len(grid[0])
        # init a grid called visited to store whether the position is visited
        visited = [[False] * n for _ in range(m)]
        # init a res var to store the number of islands with 0
        res = 0
        # impelement a expand function with inputs i, j
        def expand(i: int, j: int) -> int:
            # mark visited[i][j] = True
            visited[i][j] = True
            area = 1
            # iterate 4 directions, if the direction in range and == 1 and not on visited, dfs it
            for x, y in self.DIRECTIONS:
                new_i, new_j = i+x, j+y
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1 and not visited[new_i][new_j]:
                    area += expand(new_i, new_j)
            return area

        # run a for loop iterate m
        for i in range(m):
            # run a for loop iterate n
            for j in range(n):
                # if grid[i][j] == 1 and not visited[i][j], res += 1 and execute expand with i, j
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, expand(i, j))
        # return res as answer
        return res