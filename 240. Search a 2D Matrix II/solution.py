from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return 0
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False


class BinarySearchSolution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                left = 0
                right = n
                while left < right:
                    mid = (left + right) // 2
                    num = matrix[i][mid]
                    if num == target:
                        return True
                    elif target > num:
                        left = mid + 1
                    else:
                        right = mid
        return False
