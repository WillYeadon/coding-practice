class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        s = 0
        p = 1
        for d in digits:
            s += int(d)
            p *= int(d)
        return p - s