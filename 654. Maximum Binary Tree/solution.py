# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        max_num = max(nums)
        max_idx = nums.index(max_num)
        node = TreeNode(nums[max_idx])
        if max_idx > 0:
            node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        if len(nums) - 1 > max_idx:
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return node


class StackSolution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nodes = []
        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()
            if nodes:
                nodes[-1].right = node
            nodes.append(node)
        return nodes[0]
