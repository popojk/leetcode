# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        nodes = dfs(root)

        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nodes(mid))
            root.left, root.right = build(left, mid-1), build(mid+1, right)
            return root

        return build(0, len(nodes)-1)
