class Solution:
    def trailingZeroes(self, n: int) -> int:
        t = 0
        while n > 0:
            n //= 5
            t += n
        return t