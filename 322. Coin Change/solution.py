import math
from typing import List


class Solution:
    """
    Time: O(amount * len(coins))
    Space: O(amount)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount+1] * (amount+1)
        min_coins[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    min_coins[i] = min(min_coins[i], min_coins[i-coin] + 1)
        return min_coins[-1] if min_coins[-1] != amount+1 else -1


class TopDownDPSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(rem, cache):
            if rem < 0:
                return math.inf
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]
            cache[rem] = min(dfs(rem-x, cache) + 1 for x in coins)
            return cache[rem]

        ans = dfs(amount, {})
        return -1 if ans == math.inf else ans
