class Solution:
    def simpleFlip(self, s):
        ans = ''
        for c in s:
            if c == '1': ans += '0'
            else: ans += '1'
        return ans
    def findComplement(self, num: int) -> int:
        string = self.simpleFlip(bin(num)[2:])
        return int(string,2)