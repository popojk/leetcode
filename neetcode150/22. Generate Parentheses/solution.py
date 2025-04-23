"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # implement a dfs function accept left and right count and path as inputs, path as string, res as list
        def dfs(left: int, right: int, path: str) -> None:
            # if left and right == 0, append path and return
            if left == 0 and right == 0:
                res.append(path)
            # if left > 0, call dfs with left-1
            if left > 0:
                dfs(left-1, right, path + '(')
            # if right > left and right > 0, call dfs with right-1
            if right > left and right > 0:
                dfs(left, right-1, path + ')')
        return res
