package main

// Given a string s, return the longest palindromic substring in s.

func longestPalindrome(s string) string {
	str := []rune(s)
	dp := make([][]bool, len(str))
	var longestPal []rune

	for i := range dp {
		dp[i] = make([]bool, len(str))
	}

	// process single char
	for i, char := range str {
		dp[i][i] = true
		longestPal = []rune(string(char))
	}

	for i := len(str)-1; i >= 0; i-- {
		for j := i+1; j < len(str); j++ {
			if str[i] == str[j] {
				if j-i ==1 || dp[i+1][j-1] == true {
					dp[i][j] = true
					if j-i+1 > len(longestPal) {
						longestPal = str[i:j+1]
					}
				}
			}
		}
	}
	return string(longestPal)
}