class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        hold = bin(n)[2:][::-1]
        while len(hold) < 32:
            hold += '0'
        return int(hold, 2)
