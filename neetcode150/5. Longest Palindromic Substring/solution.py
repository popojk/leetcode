"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time: O(N^2)
        Space: O(N^2)
        """
        # int a longest_pal empty string to store result in the future
        longest_pal = ''
        # make a dp 2-D array to store isPal bool
        dp = [[False] * len(s) for _ in range(len(s))]
        # iterate s once to mark single char Pal True
        for i in range(len(s)):
            dp[i][i] = True
            longest_pal = s[i:i+1]
        # make a doube for loop to mark dp[i][j] True of False
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > len(longest_pal):
                            longest_pal = s[i:j+1]
        return longest_pal
    
class TwoPointerSolution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        # init left and right var with 0 to record max range in the future
        left = right = 0
        # implement a expand function to count max len from a given center which can be one element or two element
        def expand(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        # make a for loop to interate each char in s as center(s[i] and s[i+1] can both be center)
        for i in range(len(s)):
            # take the maximum from both results
            odd_len = expand(s, i, i)
            even_len = expand(s, i, i+1)
            # if the value is greater than current right-left, update left and righ
            curr_max_len = max(odd_len, even_len)
            if curr_max_len > right - left:
                left = i - (curr_max_len-1) // 2
                right = i + curr_max_len // 2
        # finally, return the substring of start from index left to index right
        return s[left:right+1]