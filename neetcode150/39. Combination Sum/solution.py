"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

from typing import List
import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # init a res 2D list to store results
        res = []
        # implement a back_trackfunction whch takes current_list, current_sum, target
        def back_track(current_list: list, idx: int, total: int) -> None:
            # if current_sum > target, return
            if total > target:
                return
            # if current_sum == target, append res and return
            if total == target:
                res.append(current_list)
            # make a for loop to iterate candidates
            for i in range(idx, len(candidates)):
                new_list = copy.deepcopy(current_list)
                new_list.append(candidates[i])
                back_track(new_list, i, total+candidates[i])
        back_track([], 0, 0)
        return res