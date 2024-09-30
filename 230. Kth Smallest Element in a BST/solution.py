# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, arr):
            if not root:
                return
            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)
        arr = []
        dfs(root, arr)
        return arr[k-1]


class TimeOptimizeSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        selfresult = 0
        self.dfs(root, k)
        return self.result

    def dfs(self, root, k):
        if not root:
            return
        self.dfs(root.left)
        self.count += 1
        self.result = root.val
        if self.count == k:
            return
        self.dfs(root.right)


class StackSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while True:
            while current is not None:
                stack.append(current)
                current = current.left

            if not stack:
                break

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            current = node.right
