"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
"""

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                li.append(grid[i][j])

        li.sort()
        med = li[len(li) // 2]
        ops = 0

        for num in li:
            if abs((num - med )% x) != 0:
                return -1
            ops += abs(num-med) // x
        return ops
