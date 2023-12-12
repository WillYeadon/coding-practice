class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True

        if (n // 2 == n / 2): return self.isUgly(int(n / 2))
        if (n // 3 == n / 3): return self.isUgly(int(n / 3))
        if (n // 5 == n / 5): return self.isUgly(int(n / 5))
         
        return False