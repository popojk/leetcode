from functools import cache
from typing import List


class DPSolution:

    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)

        return ans


class BackTracingSolution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start+1, len(s)+1):
                if is_pal(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        result = []
        backtrack(0, [])
        return result
