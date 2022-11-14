class graph():
    # visual
    #  s - a - b - c - - e
    #    \ |      /  \ /
    #      d - - -    f
    
    graph = {
        's' : ['a', 'd'],
        'a' : ['b', 'd'],
        'd' : ['c'],
        'b' : ['c'],
        'c' : ['f', 'e'],
        'f' : ['e'],
        'e' : [None]
        }
    
x = graph()
#print(x.graph['s'])

#for key in x.graph.keys():
#    print(key)
    
def find(graph, start, end, visited):

    for i in start:
        if i == end:
            visited.append('found')
            break
        if i is not None and i not in visited:
            visited.append(i)
        
        if i in graph.keys():
            start = graph[i]
            find(graph, start, end, visited)

def graphTest(graph, one, two):
    global visited
    if (one and two not in graph.keys()):
        return False

    start = graph[one]
    end = graph[two]

    visited = [one]

    print(visited)

    # Base case where they are the same
    if start == two:
        return True

    find(graph, start, two, visited)
    
    print(visited)
    return False

print(graphTest(x.graph, 's', 'e'))