from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def resurse(open, close, parans):
            if open == 0 and close == 0:
                res.append(parans)
                return
            if open > 0:
                resurse(open-1, close, parans + '(')
            if open < close and close > 0:
                resurse(open, close-1, parans + ')')
        resurse(n, n, '')
        return res
