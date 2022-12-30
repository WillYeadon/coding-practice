# OO Jukebox
class record():
    def __init__(self, artist, year, track):
        self.artist = artist
        self.year = year
        self.track = track
      
class jukebox():
    def __init__(self):
        self.library = []
        
    def addRecord(self, record):
        self.library.append(record)
        
    def printLibary(self):
        for i in self.library:
            print(i.artist, i.track)
            
masterFunk = jukebox()
TheDoors = record('The Doors', 1967, 'Break on through')

masterFunk.addRecord(TheDoors)
masterFunk.printLibary()