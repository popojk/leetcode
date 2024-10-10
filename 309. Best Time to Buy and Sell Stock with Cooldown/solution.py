from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            # day trade is not allowed
            return 0
        b = [-10 ** 9] * n
        s = [0] * n
        for i in range(n):
            s[i] = max(s[i-1], prices[i]+b[i-1])
            b[i] = max(b[i-1], s[i-2]-prices[i])
        return s[-1]
