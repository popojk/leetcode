from collections import deque
from typing import List


class DFSSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """時間複雜度O(R * C)，空間複雜度O(R * C)"""
        if not heights:
            return []
        R = len(heights)
        C = len(heights[0])
        a_land = set()
        p_land = set()

        def spread(r, c, land):
            land.add((r, c))
            for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= x < R and 0 <= y < C and heights[x][y] >= heights[r][c] and (x, y) not in land:
                    spread(x, y , land)

        for i in range(R):
            spread(i, 0, a_land)
            spread(i, C-1, p_land)

        for j in range(C):
            spread(0, j, a_land)
            spread(R-1, j, p_land)

        return list(a_land & p_land)
    
class BFSSolution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """時間複雜度O(R * C)，空間複雜度O(R * C)"""
        r, c = len(heights), len(heights[0])
        p_queue = deque([[0, j] for j in range(c)] + [[i, 0] for i in range(r)])
        a_queue = deque([[i, c-1] for i in range(r)] + [[r-1, j] for j in range(c)])

        def bfs(queue):
            visited = set()
            while queue:
                x, y = queue.popleft()
                visited.add((x, y))
                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= x+dx < r and 0 <= y+dy < c:
                        if (x+dx, y+dy) not in visited:
                            if heights[x+dx][y+dy] >= heights[x][y]:
                                queue.append((x+dx, y+dy))
            return visited
        p, a = bfs(p_queue), bfs(a_queue)
        return p.intersection(a)