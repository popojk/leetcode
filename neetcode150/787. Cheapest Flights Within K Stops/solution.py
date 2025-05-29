"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a 
flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
"""

from collections import defaultdict
from typing import List



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Time limit exceeds!!!!"""
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        min_price = [float('inf')]

        def dfs(curr_node, stops, total_cost):
            # 避免超過最大停留次數
            if stops > k + 1:  # 注意這裡是 k+1 因為是經過的邊數（最多 k 次中轉 = k+1 條邊）
                return

            # 到達目的地
            if curr_node == dst:
                min_price[0] = min(min_price[0], total_cost)
                return

            # 嘗試所有鄰居
            for neighbor, price in graph[curr_node]:
                if total_cost + price >= min_price[0]:
                    continue
                dfs(neighbor, stops + 1, total_cost + price)

        dfs(src, 0, 0)
        return -1 if min_price[0] == float('inf') else min_price[0]