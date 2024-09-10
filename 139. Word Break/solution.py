from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (len(s)+1)
        max_length = len(max(wordDict, key=len))
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i-1, max(i-max_length-1, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
