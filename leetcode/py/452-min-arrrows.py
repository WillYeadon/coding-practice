from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort points by the end balloon coordinates not the start.
        points.sort(key=lambda x: x[1])
        
        # Initialize count of arrows and the end point of the first balloon.
        arrows = 1
        end = points[0][1]
        # For all of the start points before this, they'll be popped with this
        # one arrow
        
        for i in range(1, len(points)):
            # If the current balloon starts after the end of the previous balloon,
            # we need another arrow, and we update the end to this balloon's end.
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
            # elsewise can assume they're popped
        return arrows
