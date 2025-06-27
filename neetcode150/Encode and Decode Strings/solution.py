"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""

"""
strs = ["union", "ai", "flyte"]
hash_map = {
 0: "union",
 1: "ai",
 2: "flyte"
}
"""

from typing import List


class Solution:
    """
    Time: O(N)
    Space: O(N)
    """
    def __init__(self):
        self.str_map = {}

    def encode(self, strs: List[str]) -> str:
        # if not strs, return empty list
        if not strs:
            return ""
        # iterate strs
        for i, str in enumerate(strs):
            # save str in the hash_map
            self.str_map[i] = str
            # return the joined string
        return "".join(strs)
    
    def decode(self, s: str) -> List[str]:
        # init a empty list as result
        res = []
        # iterate str_map by order, and append
        map_len = len(self.str_map.keys())
        for i in range(map_len):
            res.append(self.str_map[i])
            del self.str_map[i]
        # return the list
        return res
    