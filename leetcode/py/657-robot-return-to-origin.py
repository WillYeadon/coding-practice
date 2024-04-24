class Solution:
    def judgeCircle(self, moves: str) -> bool:
        loc = {'R' : 0, 'L' : 0, 'U' : 0, 'D' : 0}
        for m in moves:
            loc[m] += 1
        return loc['R'] == loc['L'] and loc['U'] == loc['D']