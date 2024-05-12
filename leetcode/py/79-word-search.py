class Solution:
    def exist(self, board, word):
        if not board:
            return False

        height = len(board)
        width = len(board[0])
        
        def worm(x, y, index, visited):
            if index == len(word):
                return True 
            if x < 0 or x >= height or y < 0 or y >= width:
                return False
            if (x, y) in visited:
                return False
            if board[x][y] != word[index]:
                return False
            # add curr            
            visited.add((x, y))
            result = (worm(x + 1, y, index + 1, visited) or
                      worm(x - 1, y, index + 1, visited) or
                      worm(x, y + 1, index + 1, visited) or
                      worm(x, y - 1, index + 1, visited))
            # if you hit this you've either gone wrong way or found work
            # already so remove from visited
            visited.remove((x, y))
            
            return result
        
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    # set is better than list
                    if worm(i, j, 0, set()):
                        return True
        
        return False