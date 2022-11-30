from LinkedList import LinkedList
from LinkedList import Node as Nodell
from collections import deque

class binNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

D = binNode('D')
E = binNode('E')
F = binNode('F')
G = binNode('G')
B = binNode('B', D, E)
C = binNode('C', F, G)       
A = binNode('A', B, C)

# Online solution
def bintoLL(root):
    levels = {}
    q = deque()
    q.append((root, 0))
    
    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            levels[level] = LinkedList(Nodell(node))
        levels[level].append(Nodell(node))
        
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
        
    return levels
    
l1 = LinkedList(Nodell(A))
l1.append(Nodell(B))
l1.append(Nodell(C))
l1.append(Nodell(D))
l1.append(Nodell(E))
l1.append(Nodell(F))
l1.append(Nodell(G))

levels = bintoLL(A)
for i in levels:
    levels[i].printElements()

