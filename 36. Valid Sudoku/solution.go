package main

import "fmt"

// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:

// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.


func isValidSudoku(board [][]byte) bool {
    // make a map as set to store the visited string as key, value doesn't matter
	set := make(map[string]struct{})

	// loop through the 2D array, if any generated string existed in set, return false, else push key into set
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			result := board[i][j]
			if result != '.' {
				rowKey := fmt.Sprintf("row key is %d %c", i, result)
				colKey :=  fmt.Sprintf("col key is %d %c", j, result)
				boxKey := fmt.Sprintf("box key is %d %d %c", i/3, j/3, result)

				if _, exists := set[rowKey]; exists {
					return false
				}

				if _, exists := set[colKey]; exists {
					return false
				}

				if _, exists := set[boxKey]; exists {
					return false
				}
				set[rowKey] = struct{}{}
				set[colKey] = struct{}{}
				set[boxKey] = struct{}{}
			}
		}
	}
	return true
}