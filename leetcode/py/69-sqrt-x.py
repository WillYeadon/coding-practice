class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        if x == ans:
            return ans
        else:
            while (ans**2 <= x):
                ans += 1
            return ans - 1