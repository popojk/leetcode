# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.

from typing import List

"""
My thoughts:
brute force 2 for loops to iterate and get O(N^2) solution.

"""

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        Time: O(N)
        Space: O(1)
        '''
        curr_sum, max_sum, min_sum = 0, 0, 0
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < min_sum:
                min_sum = curr_sum
        return max_sum - min_sum