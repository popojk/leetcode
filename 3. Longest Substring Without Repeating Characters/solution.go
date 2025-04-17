package main

func lengthOfLongestSubstring(s string) int {
	str := []rune(s)
    windowMap := make(map[rune]struct{})
	maxLen := 0
	left := 0
	for right := 0; right < len(str); right++ {
		for _, exists := windowMap[str[right]]; exists; _, exists = windowMap[str[right]] {
			delete(windowMap, str[left])
			left++
		}
		windowMap[str[right]] = struct{}{}
		maxLen = max(maxLen, right-left+1)
	}
	return maxLen
}