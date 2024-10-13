import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq_list = list(freq.values())
        max_freq_elements_count = 0
        i = 0
        while i < len(max_freq):
            if freq_list[i] == max_freq:
                max_freq_elements_count += 1
            i += 1
        ans = ((max_freq-1) * n+1) + max_freq_elements_count
        return max(ans, len(tasks))
