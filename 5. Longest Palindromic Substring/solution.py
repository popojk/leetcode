class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pal = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_pal = s[i]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        if len(longest_pal) < len(s[i:j+1]):
                            longest_pal = s[i:j+1]
        return longest_pal


class TwoPointerSolution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i+1)
            max_len = max(odd, even)

            if max_len > end-start:
                start = i - (max_len-1) // 2
                end = i + max_len // 2
        return s[start:end+1]
