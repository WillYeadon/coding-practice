class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []       
        while True:
            hold = 0
            for i in list(str(n)):
                hold += int(i)**2
            if hold == 1:
                return True
            if hold in seen:
                return False
            n = hold
            seen.append(n)
