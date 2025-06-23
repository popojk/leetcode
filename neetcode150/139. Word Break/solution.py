"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # init a dp list with len(s)+1, where dp[0] = True
        dp = [False] * (len(s)+1)
        dp[0] = True
        # get the max_word_len of object in wordDict
        wordSet = set(wordDict)
        max_word_len = 0
        # run for loop to iterate s as idx i
        for i in range(len(s)):
            # another for loop to run from i to i - max_len or 0 as idx j
            for j in range(i, max(0, i - max_word_len), i):
                # if dp[j-1] == True and s[j:i+1] in wordDict, then mark dp[i] = True
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True
                    break
        return dp[len(s)]
    