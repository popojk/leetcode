from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 in num_set:
                continue
            current_longest = 1
            while num+current_longest in num_set:
                current_longest += 1
            max_len = max(max_len, current_longest)
        return max_len
