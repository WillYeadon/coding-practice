class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    def printNode(self):
        print(self.value)
        
#                           'a'
#                            |
#           'b'                            'c'
#            |                              |
#    'd'            'e'             'f'           'g'
#     |              |               |             |
# 'h'    'i'     'j'     'k'     'l'    'm'   'n'     'o'
#  |      |       |       |       |      |     |       |
#'p''q' 'r''s'  't'      'u'     'v'    'w'  'x''y'   'z'

p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')
u = Node('u')
v = Node('v')
w = Node('w')
x = Node('x')
y = Node('y')
z = Node('z')

h = Node('h', p, q)
i = Node('i', r, s)
j = Node('j', t)
k = Node('k', u)
l = Node('l', v)
m = Node('m', w)
n = Node('n', x, y)
o = Node('o', z)

d = Node('d', h, i)
e = Node('e', j, k)
f = Node('f', l, m)
g = Node('g', n, o)

b = Node('b', d, e)
c = Node('c', f, g)

root = Node('a', b, c)