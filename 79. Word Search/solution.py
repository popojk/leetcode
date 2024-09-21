from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(chars, row, col, visited):
            if board[row][col] != chars[0]:
                return False
            if len(chars) == 1:
                return True

            visited.add((row, col))
            chars = chars[1:]

            # go up
            if row - 1 >= 0 and (row-1, col) not in visited and search(chars, row-1, col, visited):
                return True
            # go right
            if col + 1 < len(board[0]) and (row, col+1) not in visited and search(chars, row, col+1, visited):
                return True
            # go down
            if row + 1 < len(board) and (row+1, col) not in visited and search(chars, row+1, col, visited):
                return True
            # go left
            if col - 1 >= 0 and (row, col-1) not in visited and search(chars, row, col-1, visited):
                return True

            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(word, i, j, set()):
                        return True
        return False
