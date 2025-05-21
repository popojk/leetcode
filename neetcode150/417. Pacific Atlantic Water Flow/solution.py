"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, 
south, east, and west if the neighboring cell's height is less than or equal to the current cell's height.
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

from collections import deque
from typing import List


class DFSSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time: O(M * N)
        Space: O(M * N)
        """
        if not heights: return []
        # make 2 set for a_land and p_land
        R = len(heights)
        C = len(heights[0])
        a_land = set()
        p_land = set()
        # implement a spread function to run dfs with params r, c, lend(the set)
        def spread(r: int, c: int, land: set) -> None:
            # add (r, c) into land
            land.add((r, c))
            # run spread in 4 directions if meets condition
            for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= x < R and 0 <= y < C and heights[x][y] >= heights[r][c] and (x, y) not in land:
                    spread(x, y, land)
        # iterate row to run spread from left and right side
        for i in range(R):
            spread(i, 0, p_land)
            spread(i, C-1, a_land)
        # iterate column to spread from top and buttom side
        for i in range(C):
            spread(0, i, p_land)
            spread(R-1, i, a_land)

        # the answer will be a_land & p_land
        return list(a_land & p_land)
    
class BFSSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])

        p_queue = deque([[0, i] for i in range(C)] + [[j, 0] for j in range(R)])
        a_queue = deque([[R-1, i] for i in range(C)] + [[j, C-1] for j in range(R)])

        def bfs(queue: deque) -> set:
            visited = set()
            while queue:
                r, c = queue.popleft()
                visited.add([r, c])
                for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0 <= x < R and 0 <= y < C and heights[x][y] >= heights[r][c] and (x, y) not in visited:
                        queue.append([x, y])
            return visited
        p, a = bfs(p_queue), bfs(a_queue)
        return p.intersection(a)