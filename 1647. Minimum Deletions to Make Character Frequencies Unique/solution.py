from collections import Counter
import heapq


class GreedySolution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        del_count = 0
        used_freq = set()

        for c, freq in cnt.items():
            while freq > 0 and freq in used_freq:
                del_count += 1
                freq -= 1
            used_freq.add(freq)
        return del_count


class HeapSolution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        del_count = 0
        used_freq = set()

        heap = list(cnt.values())
        heapq.heapify(heap)

        while heap:
            freq = heapq.heappop(heap)
            while freq > 0 and freq in used_freq:
                del_count += 1
                freq -= 1
            used_freq.add(freq)
        return del_count
