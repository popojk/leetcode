"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] -= 1
            
            if hash_map[num] == 0:
                del hash_map[num]
        return len(hash_map.keys()) == 0