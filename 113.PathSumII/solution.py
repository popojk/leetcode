from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSSolution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if root:
            if sum == root.val and not root.left and not root.right:
                res.append(ls + [root.val])
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
            self.dfs(root.right, sum-root.val, ls+[root.val], res)


class BFSSolution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == targetSum:
                res.append(ls)
            if curr.left:
                queue.append(
                    (curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append(
                    (curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
