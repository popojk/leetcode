from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = defaultdict(int)
        left = 0
        max_len = 0
        max_count = 0
        for right in range(len(s)):
            map[s[right]] += 1
            max_count = max(max_count, map[s[right]])
            if right - left + 1 - max_count > k:
                map[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len
