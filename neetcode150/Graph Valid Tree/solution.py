"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time: O(N + E), where N isthe number of nodes, E is the number of edges
        Space: O(N + E)
        """
        if len(edges) > (n-1): return False
        # make a non-directed graph to store all edges
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # init a visited set to store visited node
        visited = set()
        # implement a dfs function with curr_node and par_node 2 inputs, return bool to tell if this is a valid tree
        def dfs(curr_node: int, par_node: int) -> bool:
            # if curr_node is in visited, return False as it means this is a circle
            if curr_node in visited: 
                return False
            # add curr_node to visited
            visited.add(curr_node)
            # iterate adj nodes in a for loop
            for adj_node in adj[curr_node]:
                # if adj_node == par_node, we continue as it's just undirected node issue
                if adj_node == par_node:
                    continue
                # in other case, just do dfs(adj_node, curr_node)
                if not dfs(adj_node, curr_node):
                    return False
            return True
            # return dfs(0, -1) and n == len(visited)
        return dfs(0, -1), n == len(visited)
