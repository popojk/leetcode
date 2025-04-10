package main

// Given a string s of '(' , ')' and lowercase English characters.

// Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

// Formally, a parentheses string is valid if and only if:

// It is the empty string, contains only lowercase characters, or
// It can be written as AB (A concatenated with B), where A and B are valid strings, or
// It can be written as (A), where A is a valid string.

type Stack []int

func (s *Stack) Pop() int {
    if len(*s) == 0 {
        panic("stack is empty")
    }
    top := (*s)[len(*s)-1]
    *s = (*s)[:len(*s)-1]
    return top
}

func (s *Stack) Push(idx int) {
	*s = append(*s, idx)
}

func minRemoveToMakeValid(s string) string {
	stack := Stack{}
	// traverse the string, if ) appear and stack len > 0 and end of stack == (, pop the stack
	// for other cases, push the index into stack
	for idx, char := range s {
		if string(char) == "(" || string(char) == ")" {
			if len(stack) > 0 && string(char) == ")" && string(s[stack[len(stack)-1]]) == "(" {
				stack.Pop()
			} else {
				stack.Push(idx)
			}
		}
	}
	// result := []rune(s)
	// traverse stack and re-arrange string
	for i := len(stack)-1; i>=0; i-- {
		idx := stack[i]
		s = s[:idx] + s[idx+1:]
	}
	return s
}