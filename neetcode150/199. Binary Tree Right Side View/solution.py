"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def dfs(node: TreeNode, level: int) -> None:
            if not node:
                return
            if len(res) < level:
                res.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        dfs(root, 1)
        return res
    
class BFSSolution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level_len = len(q)
            for i in range(level_len):
                curr_node = q.popleft()
                if i == level_len-1:
                    res.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left) 
                if curr_node.right:
                    q.append(curr_node.right)
        return res