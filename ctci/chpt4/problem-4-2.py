# BST minimal height
class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def helper(array):
    current = Node()

    if len(array) == 1:
        current.value = array[0]
        return current

    half = len(array) // 2
#    print('len is', len(array), 'half is', half)
    if len(array) % 2 == 1:
        Middle = array[half]
        LHS = array[:half]
        RHS = array[half + 1:]
    else:
        Middle = array[half - 1]
        LHS = array[:half - 1]
        RHS = array[half:]
    
    current.value = Middle
    current.left = helper(LHS)
    current.right = helper(RHS)
    
    return current

test = [1,4,5,8,9,11,15,32,38,41,42,43,44,45,55]

point = helper(test)
print(point.value, point.left.value, point.right.value)
left = point.left
print(left.value, left.left.value, left.right.value)
right = left.right
print(right.value, right.left.value, right.right.value)