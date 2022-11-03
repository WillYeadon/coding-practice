from Stack import Stack

class MultiStack:
    def __init__(self, n):
        self.multi = []
        
        for i in range(n):
            self.multi.append(Stack())
            
    def access(self, n):
        return self.multi[n]

multi = MultiStack(3)
multi.access(0).push(1)
multi.access(0).push(2)
multi.access(1).push(3)
multi.access(1).push(4)
multi.access(2).push(5)
multi.access(2).push(6)

print(multi.access(0).peek(),\
      multi.access(1).peek(),\
      multi.access(2).peek())

three = [Stack(), Stack(), Stack()]
three[0].push('a')
three[0].push('b')
three[1].push('c')
three[1].push('d')
three[2].push('e')
three[2].push('f')

print(three[0].peek(),\
      three[1].peek(),\
      three[2].peek())
