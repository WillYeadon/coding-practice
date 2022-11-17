from Stack import Stack

class SetOfStacks:
    def __init__(self, heightMax = 3):
        self.multi = []
        self.heightMax = heightMax
        self.currentHeight = 0
        self.currentStack = 0
        self.overAllLength = 0
        self.multi.append(Stack())
            
    def access(self, n = None):
        if n == None:
            n = self.currentStack
        return self.multi[n]
    
    def popAt(self, n):
        self.overAllLength -= 1
        
        
        if self.currentHeight == 0 and self.currentStack == 0:
                return self.multi[n].pop()
        if self.currentHeight == 0:
            self.currentStack -= 1
            self.currentHeight = self.heightMax

        if self.currentStack == n:
            self.currentHeight -= 1
        
        return self.multi[n].pop()
        
    def push(self, n):
        self.currentHeight += 1
        self.overAllLength += 1
        
        if self.currentHeight > self.heightMax:
            self.currentHeight = 0
            self.currentStack += 1
            self.multi.append(Stack())

        self.access(self.currentStack).push(n)                
    
    def pop(self):
        return self.popAt(self.currentStack)
    
    def deStack(self):
        while self.overAllLength > 0:
            print('value = ', self.pop(),\
                  'stack = ', self.currentStack)
    
stacks = SetOfStacks()
# Stack 1
stacks.push(1)
stacks.push(2)
stacks.push(3)

# Stack 2
stacks.push(1)
stacks.push(2)

stacks.deStack()

print('\n\n')
stacks = SetOfStacks(5)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
# Stack two
stacks.push(1)
stacks.push(2)

print('Pop off stack 1')
# Pop off stack 1
stacks.popAt(0)

stacks.deStack()

