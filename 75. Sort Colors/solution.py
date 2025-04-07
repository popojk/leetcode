"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 

with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


from typing import List
import collections


class MySolution:
    def sortColors(self, nums: List[int]) -> None:
        r, w = 0, 0
        for num in nums:
            if num == 0:
                r += 1
            elif num == 1:
                w += 1

        for i in range(len(nums)):
            if i < r:
                nums[i] = 0
            elif i >= r and i < i+w:
                nums[i] = 1
            else:
                nums[i] = 2

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
