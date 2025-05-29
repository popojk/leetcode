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
        if not heights or not heights[0]:
            return []

        R, C = len(heights), len(heights[0])

        p_queue = deque([(0, i) for i in range(C)] + [(j, 0) for j in range(R)])
        a_queue = deque([(R-1, i) for i in range(C)] + [(j, C-1) for j in range(R)])

        def bfs(queue: deque) -> set:
            visited = set(queue)
            while queue:
                r, c = queue.popleft()
                for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0 <= x < R and 0 <= y < C and heights[x][y] >= heights[r][c] and (x, y) not in visited:
                        visited.add((x, y))
                        queue.append((x, y))
            return visited

        p, a = bfs(p_queue), bfs(a_queue)
        return list(map(list, p & a))