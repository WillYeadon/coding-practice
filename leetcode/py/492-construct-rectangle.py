import math
import numpy as np
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l, w, t = area, 1, 1
        sqrt = int(np.sqrt(area))

        while sqrt >= t:
            if (l % t == 0):
                w = t
            t += 1
        return [int(area / w), int(w)]

    def constructRectangleLoop(self, area: int) -> List[int]:
        sqrt = int(math.sqrt(area))
        # Start at the sqrt and count down!!!!
        for w in range(sqrt, 0, -1):
            if area % w == 0:
                return [area // w, w]
