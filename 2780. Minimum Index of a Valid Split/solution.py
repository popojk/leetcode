"""
An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

0 <= i < n - 1
nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.
"""


from collections import defaultdict
from typing import Counter, List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        time: O(N)
        space: O(N)
        """
        n = len(nums)

        def most_frequent(data):
            counter = Counter(data)
            max_count = -1
            max_item = None

            for k, v in counter.items():
                if v > max_count:
                    max_count = v
                    max_item = k
            return max_item, max_count
        
        dom, cnt = most_frequent(nums)
        left, right = 0, cnt
        for i in range(n):
            if nums[i] == dom:
                left+=1
                right-=1
            if left * 2 > i+1 and right *2 > n - (i+1):
                return i
        return -1