class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        squared = i * i
        squares = [squared]
        while squared < num:
            i += 1
            squared = i * i
            squares.append(squared)
        return num in squares