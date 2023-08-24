class Solution:
    def dfs(self, board, i, j, m, n):
        # check if part of contiguous 'O' island 
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return 
        board[i][j] = 'hold'
        self.dfs(board, i, j + 1, m, n)
        self.dfs(board, i, j - 1, m, n)
        self.dfs(board, i - 1, j, m, n)
        self.dfs(board, i + 1, j, m, n)

    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, m, n)
            if board[i][n-1] == 'O':
                self.dfs(board, i, n-1, m, n)
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, m, n)
            if board[m-1][j] == 'O':
                self.dfs(board, m-1, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'hold':
                    board[i][j] = 'O'