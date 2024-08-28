from collections import defaultdict
from typing import List


class SlideWindowAndHashmapSolution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        max_num = 0
        left = 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            max_num = max(max_num, right - left + 1)
        return max_num
