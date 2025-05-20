"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

"""
coin在外層 amount在內層原因:
你是「累加之前 smaller coin 得到的結果」，所以不會重複計算同樣組合。

比如：
處理 coin=1：只產生 [1+1+1]
處理 coin=2：會產生 1+2，但不會重複算 2+1，因為 2 是在 1 之後處理的。
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Time: O(N * M), where M is the number of coins
        Space: O(N)
        """
        # init a dp list with len amount + 1, which represent the combinition of coins.
        # dp[0] = 1
        dp = [0] * (amount+1)
        dp[0] = 1
        # run another for loop to iterate coins
        for coin in coins:
            # run a for loop iterate from 1 to amount
            for curr_amount in range(coin, amount+1):
                # if curr_amount - coin >= 0, dp[curr_amount] += dp[curr_amount - coin]
                if curr_amount - coin >= 0:
                    dp[curr_amount] += dp[curr_amount-coin]
        # return dp[-1] if dp[-1] >= 0 else return 0
        return dp[-1]