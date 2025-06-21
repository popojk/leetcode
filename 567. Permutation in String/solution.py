"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

"""
Note:
1. s2 len should be greater than that of s1
"""

from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s2) < len(s1), return False
        if len(s2) < len(s1):
            return False
        # init a n variable represent the length of s1
        n = len(s1)
        # init a s1 map and s2 map to store char count in window
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        for c in s1:
            s1_map[c]+=1
        for i in range(n):
            s2_map[s2[i]]+=1
        # implement a is_same_map method to compare whether 2 map are equal
        def is_same_map(map1: dict, map2: dict) -> bool:
            if len(map1) != len(map2):
                return False
            for k, v in map1.items():
                if v != map2[k]:
                    return False
            return True
        # compare 2 maps once
        if is_same_map(s1_map, s2_map):
            return True
        # iterate s2 from n
        for i in range(n, len(s2)):
            # adjust the s2_map by adding s2[i] and delete s2[i-n-1]
            s2_map[s2[i]]+=1
            s2_map[s2[i-n]]-=1
            if s2_map[s2[i-n]] == 0:
                del s2_map[s2[i-n]]
            # compare 2 map, if True then return
            if is_same_map(s1_map, s2_map):
                return True
        # return False as no permutation
        return False