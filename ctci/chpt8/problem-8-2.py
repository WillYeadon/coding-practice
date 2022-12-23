# Robic on a grid r rows x c columns and can 
# only move right and down but some cells are
# off limits; design an algorithm tk navigate
# from the top left to bottom right

route = []
start = None

def findRoute(route, direction, square):
    route.append(direction)
    
    if square.value == 'dead':
        return
    
    if square.value == 'end':
        route.append('end')
        return
    
    