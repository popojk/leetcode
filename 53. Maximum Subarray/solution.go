package main

// Given an integer array nums, find the subarray with the largest sum, and return its sum.

func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
    globalMax := nums[0]
	currentMax := nums[0]
	for i := 1; i < len(nums); i++ {
		currentMax = max(nums[i], currentMax+nums[i])
		globalMax = max(globalMax, currentMax)
	}
	return globalMax
}