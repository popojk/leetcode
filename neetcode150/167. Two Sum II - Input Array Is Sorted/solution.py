"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 

Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init left, right pointer index 0, len(numbers)-1
        left, right = 0, len(numbers)-1
        # run while loop when left < right
        while left < right:
            # if left + right > target, right index -= 1
            if numbers[left] + numbers[right] > target:
                right -= 1
            # else, left idex += 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            # return left and right index after meets target, happy!!
            else:
                return [left+1, right+1]
