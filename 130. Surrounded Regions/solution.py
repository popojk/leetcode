"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
"""

from collections import deque
from typing import List


class Solution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def solve(self, board: List[List[str]]) -> None:
        
        n, m = len(board), len(board[0])

        def dfs(row: int, col: int) -> None:
            board[row][col] = 'Y'
            for dr, dc in self.DIRECTIONS:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < n and 0 <= new_col < m and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        # Run DFS from the four boundaries
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)

        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n-1, j)

        # Convert results
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

class BFSSolution:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        n, m = len(board), len(board[0])
        q = deque()

        # enqueue and mark border 'O's as 'Y'
        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = 'Y'
                q.append((i, 0))
            if board[i][m - 1] == 'O':
                board[i][m - 1] = 'Y'
                q.append((i, m - 1))

        for j in range(m):
            if board[0][j] == 'O':
                board[0][j] = 'Y'
                q.append((0, j))
            if board[n - 1][j] == 'O':
                board[n - 1][j] = 'Y'
                q.append((n - 1, j))

        # BFS
        while q:
            row, col = q.popleft()
            for dr, dc in self.DIRECTIONS:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'O':
                    board[nr][nc] = 'Y'
                    q.append((nr, nc))

        # Convert board
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
