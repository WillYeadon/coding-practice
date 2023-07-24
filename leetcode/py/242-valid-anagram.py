class Solution:
    def map(self, s):
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        return ans

    def isAnagram(self, s: str, t: str) -> bool:
        return self.map(s) == self.map(t) 