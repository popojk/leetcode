package main

func recurse(open, close int, parens string, res *[]string) {
	// if open and close == 0, append parens to res and return
	if open == 0 && close == 0 {
		*res = append(*res, parens)
	}
	// if open > 0, recurse with open - 1
	if open > 0 {
		recurse(open-1, close, parens+"(", res)
	}
	// if open < close and close > 0, recurse with close - 1
	if open < close && close > 0 {
		recurse(open, close-1, parens+")", res)
	}
}

func generateParenthesis(n int) []string {
    res := []string{}
	recurse(n, n, "", &res)
	return res
}