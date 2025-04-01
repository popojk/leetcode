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

"""
thoughts:
1. traverse the grid once to find rotten ones as bfs starting point, and count the number of fresh amount
2. push rotten position into queue and start bfs, visited +=1 once a position pushed into queue
3. a position can be visited if it is fresh or and in the grid range, if not then don't push in queue
4. after every round of bfs, round += 1
5. in the end, check if visited == fresh amount
"""

class BFSSolution:
    DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time: O(M*N)
        SPACE: O(M*N)
        """
        fresh_amount = 0
        bfs_q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_amount += 1
                elif grid[i][j] == 2:
                    bfs_q.append((i, j))

        if fresh_amount == 0:
            return 0
        
        minutes = 0

        while bfs_q:
            round_size = len(bfs_q)
            infected = 0
            for _ in range(round_size):
                r, c = bfs_q.popleft()
                for r_add, c_add in self.DIRS:
                    new_r, new_c = r + r_add, c + c_add
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        bfs_q.append((new_r, new_c))
                        infected += 1
                        fresh_amount -= 1
            if infected > 0:
                minutes += 1

        return minutes if fresh_amount == 0 else -1
            
                    

        