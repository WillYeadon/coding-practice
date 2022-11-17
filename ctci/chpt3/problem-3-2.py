class Stack():
    def __init__(self):
        self.data = []
        self.min = None
        
    def push(self, value):
        if self.min:
            if value < self.min:
                self.min = value
        else:
            self.min = value

        self.data.append(value)
        
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
    
    def minimum(self):
        return self.min

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek(),stack.minimum())

stack.push(0)
print(stack.peek(),stack.minimum())
