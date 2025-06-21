"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init a list to store the element
        element_list = []
        # run 2 for loops, and input element if the value is not ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]
                if value != ".":
                    element_list += [(i, value), (value, j), (i // 3, j // 3, value)]
        return len(element_list) == len(set(element_list))
    