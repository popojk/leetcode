package main

type TreeNode struct {
	Val int
	Left *TreeNode
    Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	if root.Left == nil && root.Right == nil {
		return true
	}

	if root.Left != nil && root.Val < root.Left.Val {
		return false
	}

	if root.Right != nil && root.Val > root.Right.Val {
		return false
	}

	return isValidBST(root.Left) && isValidBST(root.Right)
}