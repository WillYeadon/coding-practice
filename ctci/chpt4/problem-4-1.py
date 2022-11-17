# visual
#  s - a - b - c - - e     i - j - k
#    \ |      /  \ /       |   |
#      d - - -    f        g - h 
graph = {
    's' : ['a', 'd'],
    'a' : ['s', 'b', 'd'],
    'd' : ['s', 'a', 'c'],
    'b' : ['a','c'],
    'c' : ['d', 'b', 'f', 'e'],
    'f' : ['c', 'e'],
    'e' : ['c', 'f'],
    'g' : ['i', 'h'],
    'h' : ['g', 'j'],
    'i' : ['j', 'g'],
    'j' : ['i', 'h', 'k'],
    'k' : ['j']
    }

def graphTest(graph, start, end, visited=None):
    if visited is None:
        # If a node hasn't been visited this returns
        # an empty set. This only runs the first time.
        visited = set()
    # Line will loop through the list associated with
    # each key starting at the start node given
    for node in graph[start]:
        # if it is not in the set of visited nodes, add
        # it to that set
        if node not in visited:
            visited.add(node)
            # If you've matched then you can go ahead and
            # return true here. However, if not yet then
            # call this function recursively with the
            # new set (which isn't None) using the node within
            # graph[start] as the new start hence DFS
            if node == end or graphTest(graph, node, end, visited):
                return True
    # Within the recursive call, if you haven't matched end,
    # return False, remember for node in graph[start] only runs
    # when not in visited so if not will pass false back the
    # only time true is passed up is with start == end.
    return False

print(graphTest(graph, 's', 'e'))
print(graphTest(graph, 'd', 'f'))
print(graphTest(graph, 'd', 'i'))
print(graphTest(graph, 'i', 'k'))