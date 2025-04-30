"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 

You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(N)
        Space: O(1)
        """
        # use slide window to count major char, if len(window) - major_char_count <= k, move right 1 more step, else case move left 1 step
        # init a h_map to store char count
        h_map = defaultdict(int)
        # init a max_count to store answer
        max_len = 0
        # init left and right pointer both start at idx 0
        left = 0
        # while left < right and right < len(s), keep iterateing the while loop
        for right in range(len(s)):
            # update map first
            h_map[s[right]] += 1
            # get major_char_count from map
            major_char_count = max(h_map.values())
            # if len(window) - major_char_count > k, left += 1 and update map
            if (right - left + 1) - major_char_count > k:
                h_map[s[left]] -= 1
                if h_map[s[left]] == 0:
                    del h_map[s[left]]
                left += 1
            # update global max_count
            max_len = max(max_len, right - left + 1)
        return max_len
