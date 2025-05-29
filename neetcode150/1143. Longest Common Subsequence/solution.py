"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing 
the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time: O(M*N)
        Space: O(M*N)
        """
        # make a  2D dp with len len(text2) * len(text1)
        dp = [[0] * len(text2)+1 for _ in range(len(text1)+1)]
        # run for loop to iterate text1
        for i, c1 in enumerate(text1):
            # run another for loop to iterate text2
            for j, c2 in enumerate(text2):
                # dp[i+1][j+1] will be dp[i][j]+1 if char in text1 == that in text2
                # in other case, dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
                dp[i+1][j+1] = dp[i][j]+1 if c1 == c2 else max(dp[i+1][j], dp[i][j+1])
        # the answer will be dp[-1][-1]
        return dp[-1][-1]
