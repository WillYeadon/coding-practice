class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
        while len(str(ans)) > 1:
            temp = 0
            for i in str(ans):
                temp += int(i)
            ans = temp

        return ans