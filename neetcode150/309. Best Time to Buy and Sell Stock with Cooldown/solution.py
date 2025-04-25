"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) 
with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        # implement a dfs function, in each recursion we either can buy if buying is True, otherwise we only can sell
        # we must compare profit of cool down and save the max into cache
        def dfs(idx: int, buying: bool) -> int:
            if idx >= len(prices):
                return 0
            if (idx, buying) in dp:
                return dp[(idx, buying)]
            
            cooldown = dfs(idx+1, buying)
            if buying:
                buy = dfs(idx+1, not buying) - prices[idx] # we must deduct the current day price as it is the cost to buy stock
                dp[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx+2, not buying) + prices[idx] # we must sell the 
                dp[(idx, buying)] = max(sell, cooldown)
            return dp[(idx, buying)]
        return dfs(0, True)
