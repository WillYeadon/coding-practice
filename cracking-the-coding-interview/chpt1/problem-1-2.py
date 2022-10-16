# Given two strings, check whether one is a permutation of another

def checkPerm(string1, string2):
    # Early exit is strings are not the same length
    if len(string1) != len(string2):
        return False

    hash1, hash2 = {}, {}
    
    for i in string1:
        if i in hash1:
            hash1[i] += 1
        else:
            hash1[i] = 1
    
    for i in string2:
        if i in hash2:
            hash2[i] += 1
        else:
            hash2[i] = 1

    return hash1 == hash2

strings1 = ['abcdefghij', 'Unique', 'Joe Biden', 'Donald Trump']
strings2 = ['abcdefghij', 'Repeat Repeat', 'Joe Biden', 'Barack Obama']

for i, j in zip(strings1, strings2): 
    print(checkPerm(i, j))   