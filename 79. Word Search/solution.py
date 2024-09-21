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

    class CleanSolution:
        def exist(self, board: List[List[str]], word: str) -> bool:
            def back_track(i, j, k):
                if k == len(word):
                    return True
                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                    return False

                temp = board[i][j]
                board[i][j] = ''
                # do back track
                if back_track(i+1, j, k+1) or back_track(i-1, j, k+1) or back_track(i, j+1, k+1) or back_track(i, j-1, k+1):
                    return True
                # recover back track
                board[i][j] = temp
                return False

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if back_track(i, j, 0):
                        return True
            return False
