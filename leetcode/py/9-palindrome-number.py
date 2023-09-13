class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != abs(x):
            return False
        s = str(x)
        while len(s) > 1:
            left = s[0]
            right = s[-1]
            if left != right:
                return False
            s = s[1:-1]
        return True