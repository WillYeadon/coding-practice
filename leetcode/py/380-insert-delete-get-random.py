from random import randint

class RandomizedSet:
    def __init__(self):
        self.internal = []

    def insert(self, val: int) -> bool:
        if val not in self.internal:
            self.internal.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.internal:
            self.internal.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.internal[randint(0, len(self.internal) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()