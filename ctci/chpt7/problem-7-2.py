class Employee():
    def __init__(self):
        self.state = 'free'
        
class Respondent(Employee):
    def __init__(self):
        Employee.__init__(self)
        
    def takeCall(self):
        print('Responder taking call')
        self.state = 'busy'

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        
    def takeCall(self):
        print('Manager taking call')
        self.state = 'busy'
        
class Director(Employee):
    def __init__(self):
        Employee.__init__(self)
        
    def takeCall(self):
        print('Director taking call')
        self.state = 'busy'
        
class Center():
    def __init__(self):
        self.respondent_1 = Respondent()
        self.respondent_2 = Respondent()
        self.respondent_3 = Respondent()
        self.responders = [self.respondent_1,
                           self.respondent_2,
                           self.respondent_3]
        
        self.manager_1 = Manager()
        self.manager_2 = Manager()
        self.managers = [self.manager_1,
                         self.manager_2]
        
        self.director_1 = Director()
        self.directors = [self.director_1]
        
    def dispatchCall(self):
        for i in self.responders:
            if i.state != 'busy':
                i.takeCall()
                return
            
        for j in self.managers:
            if j.state != 'busy':
                j.takeCall()
                return
            
        for k in self.directors:
            if k.state != 'busy':
                k.takeCall()
                return
            
        print('All employees busy, please hold')
            
grimsby = Center()

for i in range(8):
    grimsby.dispatchCall()