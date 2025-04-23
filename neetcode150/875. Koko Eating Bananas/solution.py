"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

import math
from typing import List



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the init right will be max(piles), which means k == amount of max piles
        # the init left will be 0
        left, right = 1, max(piles)

        # implement a can_finish method to compute whether Koko can eat all the fucking bananas
        def can_finish(k: int) -> bool:
            count = 0
            for pile in piles:
                count += math.ceil(pile / k)
            return count <= h

        # if can_finish(mid) is True, right will be mid
        while left < right:
            mid = left + (right - left) // 2
            
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return right
