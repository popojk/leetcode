package main

func max(a, b int)int {
	if a > b {
		return a
	} else {
		return b
	}
}

func characterReplacement(s string, k int) int {
    hMap := make(map[string]int)
	var maxCount int
	var maxLen int
	var left int = 0
	var str = []rune(s)

	for right := 0; right < len(str); right++ {
		hMap[string(str[right])] += 1
		maxCount = max(maxCount, hMap[string(str[right])])
		if right - left + 1 - maxCount > k {
			hMap[string(str[left])] -= 1
			left++
		}
		 maxLen = max(maxLen, right - left + 1)
	}
	return maxLen
}