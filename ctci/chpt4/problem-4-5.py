# BT is where each node has max two children
# BST is where for a node n all left nodes < n
# and all right nodes > n

class binNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a = binNode(1)
b = binNode(4)
c = binNode(2, a, b)
d = binNode(7)
e = binNode(8, d)
f = binNode(5, c, e)
g = binNode(11)
h = binNode(22)
i = binNode(15, g, h)
root_1 = binNode(10, f, i)

j = binNode(2)
k = binNode(12)
l = binNode(20)
m = binNode(4, j, k)
n = binNode(10, right=l)
root_2 = binNode(8, m, n)
        
def validateBST(root):
    state = False
    value = root.value
    RHS = []
    LHS = []
    
    def transversal(node, ans):
        
        if node is None:
            return
        
        ans.append(node.value)
        
        transversal(node.left, ans)
        transversal(node.right, ans)
    
    transversal(root.left, LHS)
    transversal(root.right, RHS)
    
    if ((max(LHS) < min(RHS)) and\
        (value < min(RHS)) and\
        (max(LHS) < value)):
        state = True
        
    print(value, LHS, RHS)
    print(state)
    return state

validateBST(root_1)
validateBST(root_2)

