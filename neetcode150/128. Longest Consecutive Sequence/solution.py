"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import Counter, List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                curr_max_len = 1
                while num + curr_max_len in num_set:
                    curr_max_len += 1
                max_len = max(max_len, curr_max_len)
        return max_len
