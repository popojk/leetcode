import heapq
from typing import List


class HeapSolution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = 0
        heap = []
        for i in range(len(capacity)):
            heapq.heappush(heap, capacity[i]-rocks[i])
        while additionalRocks > 0 and heap:
            space_left = heapq.heappop(heap)
            if additionalRocks >= space_left:
                count += 1
                additionalRocks -= space_left
            else:
                break
        return count


class SortSolution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        space_left = [cap - rock for cap, rock in zip(capacity, rocks)]
        space_left.sort()
        count = 0

        for space in space_left:
            if additionalRocks >= space:
                count += 1
                additionalRocks -= space
            else:
                break
        return count
