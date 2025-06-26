"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(N), N = number of nodes
        Space: O(N)
        """
        if not root:
            return []
        # init a res 2D list to store result
        res = []
        # init a q to do BFS, and save the root node in it
        q = deque([root])
        # while q is not empty
        while q:
            # count the level length
            level_len = len(q)
            level_values = []
            # iterate nodes within level length, save level nodes
            for _ in range(level_len):
                curr_node = q.popleft()
                level_values.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(level_values)
        # return res
        return res
    
class DFSSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # init a res to store result
        res = []
        # impelemnt a dfs function with input level and node
        def dfs(node: TreeNode, level: int) -> None:
            # if node.val == None, just return
            if not node:
                return
            if len(res) == level:
                res.append([])
            # take the value, and append it to said level in res list
            val = node.val
            res[level].append(val)
            # recurse left node
            dfs(node.left, level+1)
            # recurse right node
            dfs(node.right, level+1)
        # run dfs with level 0 and root node
        dfs(root, 0)
        # return res
        return res