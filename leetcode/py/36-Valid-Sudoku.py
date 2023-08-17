class Solution:  
    def checkRow(self, board):
        for row in board:
            count = []
            for i in row:
                if (i != '.') and (i in count):
                    return False
                count.append(i)
        return True

    def checkBox(self, board):
        boxes = []
        for i in range(0,7,3):
            for j in range(0,7,3):
                boxes.append([
                board[i][j], board[i+1][j], board[i+2][j],
                board[i][j+1], board[i+1][j+1], board[i+2][j+1],
                board[i][j+2], board[i+1][j+2], board[i+2][j+2],
                ])        
        return self.checkRow(boxes)

    def checkCol(self, board):
        cols = []
        for i in range(9):
            cols.append([row[i] for row in board])       
        return self.checkRow(cols)

    def isValidSudoku(self, board):
        return self.checkBox(board) and self.checkRow(board) and self.checkCol(board)