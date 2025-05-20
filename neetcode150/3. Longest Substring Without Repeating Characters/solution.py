"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(N)
        Space: O(M), where M is the 26 alphebet
        """
        # init a hash map to store window k, v
        window_map = defaultdict(int)
        # init a max_len var to store result
        max_len = 0
        # init left, right pointer wit 0
        left = 0
        # make a for loop start from 0 as right pointer
        for right in range(len(s)):
            # while s[right] in window_map, left += 1 and remove s[left] from window_map
            while s[right] in window_map and left <= right:
                window_map[s[left]] -= 1
                if window_map[s[left]] == 0:
                    del  window_map[s[left]]
                left += 1
            # insert s[right] into window_map
            window_map[s[right]] += 1
            # compare right-left+1 with max_len and update max_len
            max_len = max(max_len, right-left+1)
        return max_len