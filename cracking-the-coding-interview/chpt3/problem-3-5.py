import random
import copy
from Stack import Stack

# Sort a stack with no other data structures except
# a temp holding stack

class sortableStack():
    def __init__(self):
        self.Lstack = Stack()
        self.Rstack = Stack()
        
    def sort(self):
        startLength = len(self.Lstack.data)
        
        # Out loop sorts via bubbling largest each time
        # decrements each time to save excess loops
        while startLength > 1:
            self.Rstack.push(self.Lstack.pop())
            currentLength = startLength
            
            # Sorting loop
            while currentLength > 1:
                cur, can = self.Rstack.peek(), self.Lstack.peek()
                
                # Conditions are either add top of the left
                # stack directly onto the right if it is larger
                # or if the right is larger then add the top of
                # the left underneath the top of the right
                if can > cur:
                    self.Rstack.push(self.Lstack.pop())
                else:
                    temp = self.Rstack.pop()
                    self.Rstack.push(self.Lstack.pop())
                    self.Rstack.push(temp)
                currentLength -= 1
            
            # Simpler to just shift the Rstack back to L 
            currentLength = startLength
            while currentLength > 0:
                self.Lstack.push(self.Rstack.pop())
                currentLength -= 1
            startLength -= 1

    # Helper function to print as a list
    def listPrint(self):
        self.x = copy.deepcopy(self.Lstack)
        self.listed = [] 
        while not self.x.isEmpty():
            self.listed.append(self.x.pop())
        print(self.listed)

x = sortableStack()

for i in range(10):
    x.Lstack.push(random.randint(1, 50))    

x.listPrint()
x.sort()
x.listPrint()
