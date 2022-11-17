from Stack import Stack

class MyQueue():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        
    def queue(self, n):
        self.s1.push(n)
        
    def dequeue(self):
        value = self.s1.peek()
        
        while len(self.s1.data) > 0:
            if len(self.s1.data) != 1:
                self.s2.push(self.s1.pop())    
            else:
                value = self.s1.pop()
                break
            
        while len(self.s2.data) > 0:
            self.s1.push(self.s2.pop())

        return value
    
q1 = MyQueue()

for i in range(5):
    q1.queue(i)    

for i in range(5):
    print(q1.dequeue())    
        
    