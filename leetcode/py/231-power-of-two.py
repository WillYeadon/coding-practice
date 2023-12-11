class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        if n == 1 or n == 2: return True

        n /= 2
        if int(n) != n: return False

        return self.isPowerOfTwo(n)