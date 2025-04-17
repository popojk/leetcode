"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

from functools import lru_cache
import math
from typing import List


class ButtomUpSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time: O(M * N), where M is amount and N is aount of coins
        Space: O(M) which is the amount
        """
        # init a dp array form 0 to amount represent the min coin of each amount
        # each dp should be init with ammount, which means a maximum number except dp[0] which should be 0
        dp = [0] + [math.inf] * amount
        # make a for loop to iterate each amount
        for curr_amount in range(amount+1):
            # another for loop to iterate each coin
            for coin in coins:
                # if curr_amount - coin >= 0, save min(dp[i-coin]+1, dp[i] in dp[i])
                if curr_amount - coin >= 0:
                    dp[curr_amount] = min(dp[curr_amount-coin]+1, dp[curr_amount])
        # the answer will be in dp[-1], if dp[-1] == amount, that means coins cannot made up amount, return -1
        return dp[-1] if dp[-1] != math.inf else -1
    
class TopDownSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time: O(M * N), where M is amount and N is aount of coins
        Space: O(M) which is the amount
        """
        @lru_cache(maxsize=None)
        def dfs(amount: int) -> int:
            if amount == 0:
                return 0
            if amount < 0:
                return math.inf
            min_coins = math.inf
            for coin in coins:
                min_coins = min(dfs(amount-coin)+1, min_coins)
            return min_coins

        result = dfs(amount)
        return result if result != math.inf else -1 
