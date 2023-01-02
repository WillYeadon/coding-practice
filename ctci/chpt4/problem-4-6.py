class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
five = Node(5)
seven = Node(7)
nine = Node(9)
eleven = Node(11)        
        
six = Node(6, five, seven)
ten = Node(10, nine, eleven)

BST = Node(8, six, ten)

def sucessor(node):   
    if node.right is None:
        return 'End of tree'
    
    current = node.right
    while current.left is not None:
        current = current.left
    
    return current.value

print(sucessor(BST))