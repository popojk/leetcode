package main

// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
//
// If there is no future day for which this is possible, keep answer[i] == 0 instead.

type Stack []int

func (s *Stack) Pop() int {
    if len(*s) == 0 {
        panic("stack is empty")
    }
    top := (*s)[len(*s)-1]
    *s = (*s)[:len(*s)-1]
    return top
}

func (s *Stack) Push(num int) {
	*s = append(*s, num)
}

func dailyTemperatures(temperatures []int) []int {
	res := make([]int, len(temperatures))
	stack := Stack{}
	for idx, currTemp := range temperatures {
		for len(stack) > 0 && currTemp > temperatures[stack[len(stack)-1]] {
			prevIdx := stack.Pop()
			res[prevIdx] = idx - prevIdx
		} 
		stack.Push(idx)
	}
	return res
}