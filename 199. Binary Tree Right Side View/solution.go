package main

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func dfs(node *TreeNode, level int, res *[]int) {
	if node == nil {
		return
	}
	if len(*res) < level {
		*res = append(*res, node.Val)
	}
	dfs(node.Left, level+1, res)
	dfs(node.Right, level+1, res)
}

func rightSideView(root *TreeNode) []int {
	res := []int{}
	dfs(root, 1, &res)
	return res
}