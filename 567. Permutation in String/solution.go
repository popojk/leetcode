package main

func isSameMap(map1, map2 map[string]int) bool {
	if len(map1) != len(map2) {
		return false
	}
	for k, v := range map1 {
		if v != map2[k] {
			return false
		}
	}
	return true
}

func checkInclusion(s1 string, s2 string) bool {
    if len(s2) < len(s1) {
		return false
	}
	// put s1 chars is s1Map
	s1Map := make(map[string]int)
	for _, char := range s1 {
		s1Map[string(char)]++
	}
	// init s2Map
	s2Map := make(map[string]int)
	for i := 0; i < len(s1); i++ {
		s2Map[string(s2[i])]++
	}
	// compare the first window
	if isSameMap(s1Map, s2Map) {
		return true
	}
	// make a for loop start from index len(s1) to len(s2)
	// in each loop delete left most element and add one more element to the right
	for i := len(s1); i < len(s2); i++ {
		left := i-len(s1)
		right := i
		s2Map[string(s2[left])]--
		if s2Map[string(s2[left])] == 0 {
			delete(s2Map, string(s2[left]))
		}
		s2Map[string(s2[right])]++
		if isSameMap(s1Map, s2Map) {
			return true
		}
	}
	return false
}
