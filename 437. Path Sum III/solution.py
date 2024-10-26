# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    cnt = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        time: O(n ^ 2)
        space: O(n)
        """
        def dfs(root, start, sum):
            if not root:
                return
            sum -= root.val
            if sum == 0:
                self.cnt += 1
            dfs(root.left, False, sum)
            dfs(root.right, False, sum)
            if start:
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)
        dfs(root, True, targetSum)
        return self.cnt
