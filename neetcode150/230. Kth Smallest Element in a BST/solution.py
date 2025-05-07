"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time: O(N)
        Space: O(H), where H is the height of BS tree
        """
        # init count and res to store current count and final answer
        self.count, self.res = 0, None
        # implement inorder function
        def in_order(root: Optional[TreeNode]) -> None:
            # if root == None, return  
            if not root:
                return
            # recurse left node
            in_order(root.left)
            # count += 1
            self.count += 1
            # if count == k, res = root.val, and return
            if self.count == k:
                self.res = root.val
                return
            # recurse right node
            in_order(root.right)
        # execute inorder
        in_order(root)
        # return res
        return self.res
        