# Still 50/50 as girl birth means you're out
# of the pot so lots of gs to make up for b's

# 16 families
# b b b b b b b b b g g g g g g g g
# b b b b g g g g
# b b g g
# b g

from random import random

def hasGirl():
    if random() > 0.5:
        return True
    else:
        return False

def simulatePopulation(families = 0):
    boys = 1
    girls = 1
    
    for i in range(families):
        girl = False
        while not girl:
            girl = hasGirl()    
            if hasGirl():
                girls += 1
                break
            boys += 1
    
    
    return boys/girls

print(simulatePopulation(100000))