class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1: 
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
    
x = Solution()
for i in range(10):
    print(x.fib(i))
