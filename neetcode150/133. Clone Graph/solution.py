"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. 
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time: O(N + E)
        Space: O(E)
        """
        if not node:
            return node
        # init a queue and a map to store clone graph
        q, clone_map = deque([node]), {node.val: Node(node.val, [])}
        while q:
            current_node = q.popleft()
            neighbors = current_node.neighbors
            for neighbor in neighbors:
                if neighbor.val not in clone_map:
                    clone_map[neighbor.val] = Node(val=neighbor.val, neighbors=[])
                    q.append(neighbor)
                # append clone neighbor
                clone_map[current_node.val].neighbors.append(clone_map[neighbor.val])
        return clone_map[node.val]