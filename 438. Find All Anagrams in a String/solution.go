package main

func isSameMap(a, b map[string]int) bool {
	if len(a) != len(b) {
		return false
	}
	for k, v := range a {
		if b[k] != v {
			return false
		}
	}
	return true
}

func findAnagrams(s string, p string) []int {
	hMap := make(map[string]int)
	res := []int{}

	for _, char := range p {
		hMap[string(char)] += 1
	}

	if len(s) < len(p) {
		return res
	}

	windowMap := make(map[string]int)
	for _, char := range s[:len(p)] {
		windowMap[string(char)] += 1
	}
	if isSameMap(windowMap, hMap) {
		res = append(res, 0)
	}

	for i := len(p); i < len(s); i++ {
		leftChar := s[i-len(p)]
		rightChar := s[i]

		windowMap[string(leftChar)] -= 1
		if windowMap[string(leftChar)] == 0 {
			delete(windowMap, string(leftChar))
		}
		windowMap[string(rightChar)] += 1

		if isSameMap(windowMap, hMap) {
			res = append(res, i-len(p)+1)
		}
	}
	return res
}