from typing import List

class Solution:
    def checkArea(self, x1, x2, height):
        return min(height[x1], height[x2]) * (x2 - x1) 
    
    def maxArea(self, height: List[int]) -> int:
        self.left = 0
        self.right = len(height) - 1

        self.area = self.checkArea(self.left, self.right, height)
        
        while (self.left < self.right):
            self.area = max(self.area, self.checkArea(self.left, self.right, height))

            if (height[self.left] < height[self.right]):
                self.left += 1
            else:
                self.right -= 1


        return self.area