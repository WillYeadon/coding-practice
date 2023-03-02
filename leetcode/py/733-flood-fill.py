from collections import deque
from typing import List

class Solution:
    def checkValid(self, can, rows, cols, image, orig):
        one = can[0]
        two = can[1]

        if (one > rows) or (two > cols) or (one < 0) or (one < 0)\
        or (two < 0) or (two < 0):
            return False
        else:
            three = image[one][two]
            if three == orig:
                return True
            else:
                return False

    def getFour(self, sr, sc):
        return [(sr - 1, sc), (sr, sc - 1), (sr + 1, sc), (sr, sc + 1)]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        rows = len(image) - 1
        cols = len(image[0]) - 1
        queue = deque()
        change = []
        seen = []

        candidates = self.getFour(sr, sc)
        candidates.append((sr, sc)) 
        for i in candidates:
            if self.checkValid(i, rows, cols, image, orig):
                if i not in change:
                    change.append(i)
                queue.append(i)

        while len(queue) > 0:
            candidate = queue.popleft()
            if candidate not in seen:
                seen.append(candidate)
                candidates = self.getFour(candidate[0], candidate[1])
                for i in candidates:
                    if self.checkValid(i, rows, cols, image, orig):
                        if i not in change:
                            change.append(i)
                        queue.append(i)

        for i in change:
            image[i[0]][i[1]] = color

        return image
    
x = Solution()
print(x.floodFill([[0,0,0],[0,0,0]], 1, 0, 2))
print(x.floodFill([[0,0,0],[0,1,0]], 1, 1, 2))