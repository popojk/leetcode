# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path):
            if not root:
                return
            nonlocal ans
            if not root.left and not root.right:
                ans += path * 10 + root.val
                return
            dfs(root.left, path * 10 + root.val)
            dfs(root.right, path * 10 + root.val)
        ans = 0
        dfs(root, 0)
        return ans
