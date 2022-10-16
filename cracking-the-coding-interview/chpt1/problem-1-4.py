# Check whether string is pallindrom

def checkPall(string):
    hash_t = {}
    parity = len(string) % 2
    flip = True
    
    for i in string:
        if i in hash_t:
            hash_t[i] += 1
        else:
            hash_t[i] = 1
    
    if parity == 1:
        for i in hash_t:
            if (hash_t[i] == 1) and flip:
                flip = False
                hash_t[i] += 1
    
    for i in hash_t:
        if hash_t[i] != 2:
            return False
    
    return True

strings = ['hannah', 'tacocat', 'glaucoma', 
           'baddy', 'racecar', 'carrace']

for i in strings:
    print(checkPall(i))