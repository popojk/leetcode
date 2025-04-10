package main

// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

func longestConsecutive(nums []int) int {
    // create a set to store non duplicate int
	numSet := make(map[int]struct{})
	for _, num := range nums {
		numSet[num] = struct{}{}
	}
	maxLen := 0
	for k, _ := range numSet {
		// we will look up, so if k-1 in set, it meas it has already been visited, we skip to reduce time complexity
		if _, exists := numSet[k-1]; exists {
			continue
		}
		currMaxLen := 1
		for {
			if _, exists := numSet[k+currMaxLen]; exists {
				currMaxLen++
			} else {
				break
			}
		}
		maxLen = max(currMaxLen, maxLen)
	}
	return maxLen
}