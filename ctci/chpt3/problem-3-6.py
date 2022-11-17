class animal():
    def __init__(self, name, species):
        self.name = name
        self.type = species
        
    def printValues(self):
        print(self.name, self.type)
        
class shelter():
    def __init__(self):
        self.qOld = []
        self.qDog = []
        self.qCat = []
        
    def enque(self, animal):
        self.qOld.append(animal)
        if animal.type == "dog":
            self.qDog.append(animal)
        else:
            self.qCat.append(animal)
    
    def dequeHelp(self, queue):
        return (queue[0], queue[1:])
    
    def dequeAny(self):
        if self.qOld[0].type == "dog":
            self.qDog = self.dequeHelp(self.qDog)[1]
        else:
            self.qCat = self.dequeHelp(self.qCat)[1]
        value, self.qOld = self.dequeHelp(self.qOld)
        return value       
    
    def dequeDog(self):
        if self.qOld[0].type == "dog":
            self.qOld = self.dequeHelp(self.qOld)[1]
        value, self.qDog = self.dequeHelp(self.qDog)
        return value
        
    def dequeCat(self):
        if self.qOld[0].type == "cat":
            self.qOld = self.dequeHelp(self.qOld)[1]
        value, self.qCat = self.dequeHelp(self.qCat)
        return value   

shelter = shelter()
shelter.enque(animal("larry", "cat"))
shelter.enque(animal("barry", "dog"))
shelter.enque(animal("oscar", "cat"))
shelter.enque(animal("foxtrot", "cat"))
shelter.enque(animal("boxxer", "dog"))
shelter.enque(animal("rocky", "dog"))
shelter.enque(animal("charlie", "cat"))

shelter.dequeAny().printValues()
shelter.dequeCat().printValues()
shelter.dequeAny().printValues()



        