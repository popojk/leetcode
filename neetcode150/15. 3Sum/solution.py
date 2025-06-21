"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

"""
the min len is 3, so we don't need to worry about out of range issue
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time:  O(N ^ 2)
        Space: O(N ^ 2)
        """
        # init a list to store result
        res = []
        # sort nums to run two pointer
        nums.sort()
        # run a for loop to iterate nums, the number represent fixed pointer
        for i, a in enumerate(nums):
            # if the pointer > 0, breake for loop as it is not possible to compose answer
            if a > 0:
                break
            # if the pointer == nums[i-1], continue as it will cause duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # init l, r with i+1, len(nums)-1
            l, r = i+1, len(nums)-1
            # run while loop when l < r
            while l < r:
                # count sum first
                sum = a + nums[l] + nums[r]
                # if sum > 0, r -=1
                if sum > 0:
                    r -= 1
                # if sum < 0, l += 1
                elif sum < 0:
                    l += 1
                # else case append answer
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    # while nums[l] == nums[l-1], l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
