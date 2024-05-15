from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int: 
        out = [0] * (n)   
        inc = [0] * (n)   

        for t in trust:
            inc[t[0] - 1] += 1
            out[t[1] - 1] += 1

        for i in range(n):
            if inc[i] == 0 and out[i] == n - 1:
                return i + 1
        return -1