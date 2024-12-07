from typing import List


class Solution:
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