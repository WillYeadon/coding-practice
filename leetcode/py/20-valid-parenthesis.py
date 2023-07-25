class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = ['()','{}','[]']
        for i in s:
            x = ''
            if stack:
                x = stack[-1] + i 
            stack.append(i)
            if x in brackets:
                stack.pop(), stack.pop()

        if not stack:
            return True
        else:
            return False