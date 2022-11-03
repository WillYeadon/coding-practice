class Stack():
    def __init__(self):
        self.data = []
        
    def push(self, value):
        self.data.append(value)
        
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]
        