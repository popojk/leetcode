package main

// You are given an integer array height of length n.

// There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, such that the container contains the most water.

// Return the maximum amount of water a container can store.

// Notice that you may not slant the container.

func minHeight(leftHeight, rightHeight int) int {
	if leftHeight <= rightHeight {
		return leftHeight
	} else {
		return rightHeight
	}
}

func maxArea(height []int) int {
	// Time: O(N)
	// Space: O(1)
    left := 0
	right := len(height) - 1
	maxAmount := 0
	
	for left < right {
		area := minHeight(height[left], height[right]) * (right - left)
		if area > maxAmount {
			maxAmount = area
		}
		if height[left] <= height[right]{
			left++
		} else {
			right--
		}
	}
	return maxAmount
}