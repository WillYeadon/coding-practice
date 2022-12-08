class binNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
one = binNode(1)
four = binNode(4)
two = binNode(2, one, four)
seven = binNode(7)
eight = binNode(8, seven)
five = binNode(5, two, eight)
eleven = binNode(11)
twentyT = binNode(22)
fifT = binNode(15, eleven, twentyT)
root = binNode(10, five, fifT)

def balanced(root):
    L_height = 0
    R_height = 0
    current = root
    
    while current.left is not None:
#        print(current.value)
        L_height += 1
        current = current.left

    current = root
    while current.left is not None:
#        print(current.value)
        R_height += 1
        current = current.right
        
    if current.left is not None:
        R_height += 1
    
#    print(L_height, R_height)
    if abs(L_height - R_height) <= 1:
        return True
    else:
        return False
    
print(balanced(root))