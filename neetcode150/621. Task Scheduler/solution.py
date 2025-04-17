"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 

Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, 
but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
"""

from collections import Counter
from typing import List
import heapq
import collections


class PriorityQueueSolution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # init a max heap to store all freq
        freq = Counter(tasks)
        heap = []
        # init a deque to store cool down freq
        cooldown = collections.deque()
        # init a timer to record current time
        timer = 0
        # init the heap
        for _, v in freq.items():
            heapq.heappush(heap, -v) 
        # process heap or cooldown if they are not nil
        while heap or cooldown:
            # process heap
            if heap:
                task = -heapq.heappop(heap)
                if task > 1:
                    cooldown.append((task-1, timer+n+1))
            # time += 1
            timer += 1
            # process cooldown if cool down time meets
            while cooldown and cooldown[0][1] == timer:
                task, _ = cooldown.popleft()
                heapq.heappush(heap, -task)
        return timer
