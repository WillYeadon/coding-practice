class Solution:
    def create(self, s):
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        return ans

    def findTheDifference(self, s: str, t: str) -> str:
        one = self.create(s)
        two = self.create(t)

        for key in two.keys():
            if key not in one:
                return key
            elif one[key] != two[key]:
                return key
        return