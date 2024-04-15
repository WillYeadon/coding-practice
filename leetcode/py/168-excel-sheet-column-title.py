class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            carry = (columnNumber - 1) % 26
            ans = chr(carry + 65) + ans  
            columnNumber = (columnNumber - 1) // 26  
        return ans