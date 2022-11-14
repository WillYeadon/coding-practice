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

for key in x.graph.keys():
    print(key)