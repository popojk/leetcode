"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time: O(N ^ 2)
        Space: O(N ^ 2)
        """
        # init a 2D dp list to store if dp[i][j](s[i] ~ s[j]) is pal
        dp = [[False] * len(s) for _ in range(len(s))]
        # init a res with 0 to store result
        res = 0
        # fulfill dp for each single char
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        # run a for loop with i = len(s)-1
        for i in range(len(s)-1, -1, -1):
            # run another for loop with j = i+1
            for j in range(i+1, len(s)):
                # if s[i] == s[j], do bellow
                if s[i] == s[j]:
                    # if dp[i-1][j+1] == True or i-j == 1, res += 1, dp[i][j] = True
                    if dp[i+1][j-1] or j-i == 1:
                        dp[i][j] = True
                        res += 1
        # return res as answer
        return res
    
class TwoPointerSolution:
    """
    Time: O(N ^ 2)
    Space: O(N ^ 2)
    """
    def expand(self, i: int, j: int, s: str):
        cnt = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cnt+=1
            i-=1
            j+=1
        return cnt

    def countSubstrings(self, s: str) -> int:
        return sum(self.expand(i, i, s) + self.expand(i, i+1, s) for i in range(len(s)))
