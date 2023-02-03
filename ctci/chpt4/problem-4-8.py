from TreeStructure import *

#                           'a'
#                            |
#           'b'                            'c'
#            |                              |
#    'd'            'e'             'f'           'g'
#     |              |               |             |
# 'h'    'i'     'j'     'k'     'l'    'm'   'n'     'o'
#  |      |       |       |       |      |     |       |
#'p''q' 'r''s'  't'      'u'     'v'    'w'  'x''y'   'z'

# Find first common ancestor

def dfs(node, value, path):
    # Exit if none is None
    if node is None:
        return None
    # If you've found the value can return recursion
    if node.value == value:
        return path + [node.value]
    # Recurse left
    left_path = dfs(node.left, value, path + [node.value])
    # If this left_path doesn't end in None return
    # it as prior statements return None unless
    # value is found
    if left_path is not None:
        return left_path
    # Value not on left so look right
    right_path = dfs(node.right, value, path + [node.value])
    if right_path is not None:
        return right_path
    # Catch at the end if not in there
    return None    

def dfsAnc(node, n1, n2):
    # Node not found so False returned also
    if node is None:
        return None, False
    # If not is found return it and True
    if node.value == n1:
        return node, True
    if node.value == n2:
        return node, True
    # Look left
    left_node, left_found = dfsAnc(node.left, n1, n2)
    # Not working....
    if left_node is not None:
        if left_found:
            return left_node, True
        right_node, right_found = dfsAnc(node.right, n1, n2) 
        if right_found:
            return node, True
        return left_node, False
    right_node, right_found = dfsAnc(node.right, n1, n2)
    if right_node is not None:
        return right_node, right_found
    # Nodes are not in there
    return None, False

def lca(node, n1, n2):
    # Call return lca node if present and bool
    # flag to indicate
    lca, found = dfsAnc(node, n1, n2)
    # If you have found a last common ancestor, return it
    if found:
        return lca.value
    # Not found so return None
    return None
    
#print(dfs(root, 'y', []))
print(lca(root, 'r', 'k'))
print(lca(root, 'w', 'q'))
print(lca(root, 'Not in a', 'Not in b'))