class SolutionA:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(st):
            st = list(st)
            while '#' in st:
                for i, v in enumerate(st):
                    if v == '#':
                        if i == 0:
                            del st[0]
                            break
                        else:
                            del st[i-1:i+1]
                            break                          
            return st

        if helper(s) == helper(t):
            return True
        else:
            return False

class SolutionB:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process(s) == self.process(t)

    def process(self, word):
        # Empty stack
        stack=[]
        for ch in word:
            # if # and not empty stack then delete the character
            # on the top e.g. backspace
            if ch == '#' and stack:
                stack.pop()
            # else add it to the stack
            elif ch!='#':
                stack.append(ch)
        # Return joint stack
        return ''.join(stack)

x = SolutionA()
print(x.backspaceCompare('a##c', '#a#ce'))
print(x.backspaceCompare('bxj##tw', 'bxo#j##tw'))
y = SolutionB()
print(y.backspaceCompare('a##c', '#a#ce'))
print(y.backspaceCompare('bxj##tw', 'bxo#j##tw'))