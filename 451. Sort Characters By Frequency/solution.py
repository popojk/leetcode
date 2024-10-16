import collections
import heapq


class HeapSolution:
    def frequencySort(self, s: str) -> str:
        """
        time: O(n log k), k refers to the number of distinct numbers
        space: O(n)
        """
        count = collections.Counter(s)
        heap = []

        for c, freq in count.items():
            heapq.heappush(heap, (-freq, c))

        ans = []
        while heap:
            freq, c = heapq.heappop(heap)
            ans += [c] * -freq
        return ''.join(ans)


class HashMapSolution:
    def frequencySort(self, s: str) -> str:
        """
        time: O(n log n)
        space: O(n)
        """
        count = collections.Counter(s)

        res = []
        for k, v in sorted(count.items(), key=lambda x: -x[1]):
            res += [k] * v
        return ''.join(res)
