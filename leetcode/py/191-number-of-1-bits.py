class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(int, list(str(bin(n))[2:])))