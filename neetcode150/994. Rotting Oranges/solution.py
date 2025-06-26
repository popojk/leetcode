"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from collections import deque
from typing import List


class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time: O(N * M)
        Space: O(N * M)
        """
        # init a q for running BFS
        q = deque()
        n, m = len(grid), len(grid[0])
        # count how many fresh first
        fresh = 0
        # at the same time save (i, j) into q for rotten ones
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.appendleft((i, j))
        # init a round var to to count minutes
        round = 0
        # while q not empty, do bfs
        while q and fresh > 0:
            round_len = len(q)
            round += 1
            for _ in range(round_len):
                x, y = q.pop()
                for new_x, new_y in ((x+x1, y+y1) for x1, y1 in self.DIRECTIONS):
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh -= 1
                        q.appendleft((new_x, new_y))
        # if fresh != 0, return -1, else round
        return -1 if fresh != 0 else round
