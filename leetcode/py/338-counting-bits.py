class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(n + 1):
            s = str(bin(i))
            for one in s:
                if one == '1':
                    ans[i] += 1
        return ans