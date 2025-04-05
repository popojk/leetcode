from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        """
        curr_max, curr_min = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n*curr_max, n*curr_min)
            curr_max, curr_min = max(vals), min(vals)

            res = max(res, curr_max)
        return res
