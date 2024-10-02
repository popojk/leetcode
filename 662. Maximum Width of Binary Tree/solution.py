# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = [(0, root)]

        while queue:
            n = len(queue)
            nodes = []
            for _ in range(n):
                idx, node = queue.pop(0)
                if node.left:
                    queue.append((2*idx+1, node.left))
                if node.right:
                    queue.append((2*idx+2, node.right))
                nodes.append(idx)
            ans = max(ans, max(nodes) - min(nodes) + 1)
        return ans


class DFSSolution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)

        def dfs(node, level, column):
            if node:
                di[level].append(column)
                dfs(node.left, level+1, column*2)
                dfs(node.right, level+1, column*2+1)
        dfs(root, 0, 0)
        return max([max(di[level]) - min(di[level]) + 1 for level in di])
