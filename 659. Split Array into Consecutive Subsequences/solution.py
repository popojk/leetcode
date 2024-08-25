import collections
import heapq
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        dikt = collections.defaultdict(list)

        for i in range(n):
            num = nums[i]

            if not dikt[num-1]:
                heapq.heappush(dikt[num], 1)
            else:
                l = heapq.heappop(dikt[num-1])
                heapq.heappush(dikt[num], l+1)
        for arr in dikt.values():
            for l in arr:
                if l < 3:
                    return False
        return True


class SolutionB:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)  # 對數組中的元素進行計數

        for i in sorted(counter.keys()):  # 對有不同值的元素排序後進行迭代
            while counter[i] > 0:  # 當當前元素的計數大於0時，嘗試構建序列
                last = 0
                j = i
                k = 0
                while counter[j] >= last:  # 構建一個連續的子序列
                    last = counter[j]
                    counter[j] -= 1
                    j += 1
                    k += 1
                if k < 3:  # 如果構建的序列長度小於3，則返回 False
                    return False
        return True  # 如果所有元素都可以構建成長度至少為3的連續子序列，則返回 True
