"""
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.
"""

import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_handle_all(time: int) -> bool:
            """return whether can handle all car in given time"""
            acc_cars = 0
            for rank in ranks:
                acc_cars += math.floor(math.sqrt(time / rank))
                if acc_cars >= cars:
                    return True
            return False

        min_time, max_time = 0, max(ranks) * cars * cars
        while min_time < max_time:
            time = min_time + (max_time - min_time) // 2
            if can_handle_all(time):
                max_time = time
            else:
                min_time = time + 1
        return min_time