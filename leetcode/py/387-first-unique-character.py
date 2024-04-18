class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1: return 0
        seen = {}
        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1