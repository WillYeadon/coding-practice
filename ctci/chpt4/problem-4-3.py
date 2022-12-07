from collections import deque

class linkedListNode():
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
        
class linkedList():
    def __init__(self, node):
        self.head = node
        
    def append(self, new_node):
        current = self.head
        
        if (self.head):
            while (current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def printElements(self):
        current = self.head
        
        while current.next:
            print(current.value)
            current = current.next

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
            levels[level] = linkedList(linkedListNode(node))
        levels[level].append(linkedListNode(node))
        
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
        
    return levels
    
l1 = linkedList(linkedListNode(A))
l1.append(linkedListNode(B))
l1.append(linkedListNode(C))
l1.append(linkedListNode(D))
l1.append(linkedListNode(E))
l1.append(linkedListNode(F))
l1.append(linkedListNode(G))

levels = bintoLL(A)
print(levels[1].head.value.value)
#for i in levels:
#    levels[i].printElements()

test = [1, 2, 3]
#for i in test:
#    print(i)
#    test.append(i) 

