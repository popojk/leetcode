"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time: O(n * k log k)
        Space: O(n * k)
        """
        # init a hash map with k: v pair sorted_string: result_list
        h_map = defaultdict(list)
        # run a for loop to iterate each string in strs
        for word in strs:
            # in each iteration, sort the string first
            sorted_word = ''.join(sorted(word))
            # append word to given key
            h_map[sorted_word].append(word)
        # return list of hash map values
        return list(h_map.values())
        
        
