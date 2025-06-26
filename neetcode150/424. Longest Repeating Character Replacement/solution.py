"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 

You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        global_max = 0
        window_map = defaultdict(int)
        left = 0
        for right in range(len(s)):
            # update right window first
            window_map[s[right]] += 1
            # get max_char_len 
            max_char_len = max(window_map.values())
            # check if window valid
            if right - left + 1 - max_char_len > k:
                # if not valid, update left window
                window_map[s[left]] -= 1
                if window_map[s[left]] == 0:
                    del window_map[s[left]]
                left += 1
            global_max = max(global_max, right - left + 1)
        return global_max
