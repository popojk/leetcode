from typing import List
import collections


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = collections.Counter(nums)
        idx = 0
        for color in range(3):
            freq = count.get(color, 0)
            nums[idx: idx+freq] = [color] * freq
            idx += freq
