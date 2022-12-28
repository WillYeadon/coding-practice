# Robic on a grid r rows x c columns and can 
# only move right and down but some cells are
# off limits; design an algorithm tk navigate
# from the top left to bottom right

# trick here is that to get to the last square you 
# need to get to the second to last square. You
# can go to either row - 1 or col - 1 on each call
# pyramiding out

route = []

def findRoute(row, col, route):
    # Checks you're in the maze & stops inf loop
    if row < 0 or col < 0:
        return False
    
    # Base case
    origin = (row == 0) and (col == 0)
       
    if (origin or \
        findRoute(row - 1, col, route) or \
        findRoute(row, col - 1, route) ):
        point = (row, col)
        route.append(point)
        return True

    return False
    
findRoute(3,3, route)
print(route)