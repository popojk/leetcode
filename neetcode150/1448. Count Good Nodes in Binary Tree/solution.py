"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time: O(N)
        Space: O(N) ~ O(log N), depends on the depth of tree
        """
        res = 0

        def dfs(node: TreeNode, current_max: int):
            nonlocal res
            if not node:
                return
            if node.val >= current_max:
                res += 1
            current_max = max(current_max, node.val)
            dfs(node.left, current_max)
            dfs(node.right, current_max)

        dfs(root, root.val)
        return res