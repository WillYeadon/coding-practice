# Build order

# a b c d e f
# (a,d), (f,b), (b,d), (f,a), (d,c)

class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
        #print(self.value)

# So it wants you to find an algorithm that will create this here
# Given the dependencies.
f = node('f')
e = node('e')
a = node('a', f)
b = node('b', f)
d = node('d', a, b)
c = node('c', d)

dependencies = [(a,d), (f,b), (b,d), (f,a), (d,c)]
for i in dependencies:
    print(i[0].value, i[1].value)
