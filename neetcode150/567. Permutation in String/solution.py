"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time Complexity: O(n), where n is the length of s2
        - Building s1_map takes O(m) time, where m is the length of s1
        - Building initial window takes O(m) time
        - Sliding window operations take O(n-m) time
        - Each is_same_map call takes O(1) time (assuming fixed character set size)
        
        Space Complexity: O(k), where k is the size of the character set
        - s1_map uses O(k) space to store character frequencies
        - s2_window uses O(k) space to store character frequencies
        - For English lowercase letters, k = 26, so space complexity is effectively O(1)
        """
        # 如果 s1 比 s2 長，不可能找到排列
        if len(s1) > len(s2):
            return False
            
        def is_same_map(a: dict, b: dict) -> bool:
            if len(a.keys()) != len(b.keys()):
                return False
            for k, v in a.items():
                if k not in b or b[k] != v:
                    return False
            return True
            
        # 建立 s1 的字符頻率表
        s1_map = defaultdict(int)
        for c in s1:
            s1_map[c] += 1
            
        # 建立 s2 初始窗口的字符頻率表
        s2_window = defaultdict(int)
        for i in range(len(s1)):
            s2_window[s2[i]] += 1
            
        # 檢查初始窗口
        if is_same_map(s1_map, s2_window):
            return True
            
        # 滑動窗口檢查剩餘部分
        for i in range(len(s1), len(s2)):
            # 移除窗口左側字符
            s2_window[s2[i-len(s1)]] -= 1
            if s2_window[s2[i-len(s1)]] == 0:
                del s2_window[s2[i-len(s1)]]
                
            # 添加窗口右側新字符
            s2_window[s2[i]] += 1
            
            # 檢查當前窗口
            if is_same_map(s1_map, s2_window):
                return True
                
        return False
