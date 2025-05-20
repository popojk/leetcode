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
        Time: O(N^2)
        Space: O(M), where M is the size of response list
        """
        # int a lists on list to store results
        res: List[List[int]] = []
        # sort the list 
        nums.sort()
        # run a for loop to iterate i from 0 to len(nums)
        for i, a in enumerate(nums):
            # if a > 0, break the loop as it is impossible to sum 0
            if a > 0:
                break
            # if i > 0 and nums[i-1] == a, countinue the loop
            if i > 0 and nums[i-1] == a:
                continue
            # init l, r with i+1, len(nums)-1
            l, r = i+1, len(nums)-1
            # while l < r, iterate
            while l < r:
                sum = a + nums[l] + nums[r]
                # if 3 sum > 0, r -= 1
                if sum > 0:
                    r -= 1
                # elif 3 sum < 0, l += 1
                elif sum < 0:
                    l += 1
                # else case, append idx list to list
                else:
                    res.append([a, nums[l], nums[r]])
                    # i+=1, l-=1
                    l+=1
                    r-=1
                    # while nums[l] == nums[l-1] and l < r, l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        # return res
        return res
