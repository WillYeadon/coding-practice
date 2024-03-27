class Solution:
    def convertToBase7(self, num: int) -> str:
        add = ""
        if num < 0: add = "-"
        num = abs(num)
        ans = ""
        sevens = [40353607,5764801,823543,117649,16807,2401,343,49,7]
        i = 0
        while i < 9:
            div = sevens[i]
            count = 0
            while num >= div:
                num -= div
                count += 1
            i += 1
            ans += str(count)
        ans = str(int(ans + str(num)))
        return add + ans