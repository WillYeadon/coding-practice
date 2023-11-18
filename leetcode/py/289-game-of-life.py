from typing import List

class Solution:
    def logic(self, val, count):
        if val == 1:
            if count == 2 or count == 3: 
                return 1
        else:
            if count == 3:
                return 1
        return 0

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        newBoard = [[0] * len(board[0]) for _ in range(len(board))]
        height = len(newBoard)
        width = len(newBoard[0])

        for i in range(height):
            for j in range(width):
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue

                        ni, nj = i + di, j + dj
                        if 0 <= ni < height and 0 <= nj < width:
                            count += board[ni][nj]
                newBoard[i][j] = self.logic(board[i][j], count)
        for i in range(height):
            for j in range(width):
                board[i][j] = newBoard[i][j]       