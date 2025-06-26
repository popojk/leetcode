"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(N)
        Space: O(log N) - O(N), in case the tree cannot be balanced
        """
        # impelement a dfs function with node, min, max input and return bool to tell if the node is valid
        def is_valid(node: TreeNode, min: int, max: int) -> bool:
            # if node is None, return True as it is the end of leaf node
            if not node:
                return True
            # if not min < node.val < right, return False
            if not (min < node.val < max):
                return False
            # check if left node and right node are both valid and return result
            # root.val will be the middle value to run DFS
            return is_valid(node.left, min, node.val) and is_valid(node.right, node.val, max)
        # return value of dfs with root, float('-inf), float('inf) input
        return is_valid(root, float('-inf'), float('inf'))
    
class BFSSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # init a queue to run BFS, each element contains (node, min, max)
        q = deque([(root, float('-inf'), float('inf'))])
        # while q not empty, iterate
        while q:
            # pop out element
            node, min, max = q.popleft()
            # if not min < node.val < max, just return False right away
            if not (min < node.val < max):
                return False
            # enque left node
            if node.left:
                q.append((node.left, min, node.val))
            # enque right node
            if node.right:
                q.append((node.right, node.val, max))
        # return True in the end
        return True