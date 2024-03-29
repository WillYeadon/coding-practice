class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = []
        val = 0
        for c in columnTitle[::-1]:
            ans.append(ord(c) - 64)
        for i,v in enumerate(ans):
            val += v * pow(26, i)
        return val
        