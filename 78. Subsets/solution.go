package main

// Given an integer array nums of unique elements, return all possible subsets (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

func backTrack(idx int, path []int, nums []int, res *[][]int) {
	// if idx > maxLen, terminate the recursion
	pathCopy := make([]int, len(path))
	copy(pathCopy, path)
	*res = append(*res, pathCopy)

	for i := idx; i < len(nums); i++ {
		path = append(path, nums[i])
		backTrack(i+1, path, nums, res)
		path = path[:len(path)-1]
	}
}

func subsets(nums []int) [][]int {
	res := [][]int{}
	backTrack(0, []int{}, nums, &res)
	return res
}