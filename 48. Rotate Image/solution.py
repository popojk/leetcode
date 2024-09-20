from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp_result = [[] for _ in range(n)]
        for i in range(n):
            temp_list = []
            for j in range(n-1, -1, -1):
                temp_list.append(matrix[j][i])
            temp_result[i] = temp_list
        for i in range(n):
            matrix[i] = temp_result[i]


class NoExtraSpaceSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
