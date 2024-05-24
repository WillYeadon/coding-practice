from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = {}
        for i in edges:
            if i[0] in seen:
                return i[0]
            elif i[1] in seen:
                return i[1]
            else:
                seen[i[0]] = 1
                seen[i[1]] = 1