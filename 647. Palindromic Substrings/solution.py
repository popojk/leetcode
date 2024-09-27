class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[False for _ in range(len(s))] for __ in range(len(s))]

        for i in range(len(s)):
            for j in range(i):
                if i - j <= 2:
                    dp[j][i] = s[j] == s[i]
                else:
                    dp[j][i] = s[j] == s[i] and dp[j+1][i-1]
                if dp[j][i]:
                    count += 1
            dp[i][i] = True
            count += 1
        return count


class SecondSolution:
    def expand(self, i, j, s):
        length = len(s)
        cnt = 0
        while i >= 0 and j < length and s[i] == s[j]:
            i -= 1
            j += 1
            cnt += 1
        return cnt

    def countSubstrings(self, s: str) -> int:
        return sum(self.expand(i, i, s) + self.expand(i, i+1, s) for i in range(len(s)))
