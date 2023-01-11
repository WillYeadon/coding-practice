from random import randint
# OOP carpark

class vehicle():
    def __init__(self, size):
        self.size = size
        
    def printSize(self):
        print(self.size)

class car(vehicle):
    def __init__(self, size, make, model):
        super().__init__(size)
        self.make = make
        self.model = model
    
    def printCar(self):
        print(self.make,
              self.model)
        
class carPark():
    def __init__(self, x, y):
        self.length = x
        self.width = y
        print(x, y)
        self.spaces = self.createSpace(x, y)
    
    def createSpace(self, x, y):
        spaces = []
        for i in range(self.width):
            spaces.append(['Empty' for _ in range(self.length)])
              
        return spaces
            
    def printSpaces(self):
        for i in self.spaces:
            print(i)
            
    def park(self, car):
        parked = False
        
        while not parked:      
            y = randint(0, self.length - 1)
            x = randint(0, self.width - 1)

            if self.spaces[x][y] == 'Empty':
                self.spaces[x][y] =\
                    car.make + ' ' + car.model
                parked = True

boj = car('Small', 'Vaxhaull', 'Corsa')

pods = carPark(4, 3)
pods.printSpaces()
print()
pods.park(boj)
pods.printSpaces()
