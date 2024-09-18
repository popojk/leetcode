from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_col = [False] * m
        zero_row = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_col[i] = True
                    zero_row[j] = True
        for i in range(m):
            for j in range(n):
                if zero_col[i] or zero_row[j]:
                    matrix[i][j] = 0
