package main

// Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

// Note that the same word in the dictionary may be reused multiple times in the segmentation.

func wordBreak(s string, wordDict []string) bool {
	// O(m * maxLen)
	// O(n + m), n = len of s, m = len of wordDict
    str := []rune(s)
    // this map is constructed to improve search Time complexity to O(1)
    wordDictStr := make(map[string]bool)
    for _, word := range wordDict {
        wordDictStr[word] = true
    }

    dp := make([]bool, len(str)+1)
    dp[0] = true  // Empty string is always a valid word break
    maxLen := 0

    // Precompute the maximum word length
    for _, word := range wordDict {
        if len(word) > maxLen {
            maxLen = len(word)
        }
    }

    // Dynamic programming to check possible word breaks
    for i := 1; i <= len(str); i++ { // Start from i=1 to len(str)
        for j := i - 1; j >= max(i-maxLen, 0); j-- {
            if dp[j] == true {
                if wordDictStr[string(str[j:i])] {
                    dp[i] = true
                    break
                }
            }
        }
    }

    return dp[len(str)] // Corrected the index
}