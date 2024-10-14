import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """時間複雜度O(T)，空間複雜度O(1)"""
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


class HeapSolution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """時間複雜度O(timer*logk)，空間複雜度O(N)"""
        freq = collections.Counter(tasks)
        heap = []
        cooldown = collections.deque()
        timer = 0

        # create max heap
        for k, v in freq.items():
            heapq.heappush(heap, -v)

        while heap or cooldown:
            if heap:
                task = -heapq.heappop(heap)
                if task > 1:
                    cooldown.append((task-1, timer+n+1))
            timer += 1
            while cooldown and cooldown[0][1] == timer:
                task_count, _ = cooldown[0]
                cooldown.popleft()
                heapq.heappush(heap, -task_count)
        return timer
