# check if two strings are one (or zero) edits away from each other
# check for insert, replace over or remove

def oneAway(string1, string2):
    if (string1 == string2):
        return True
    
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

    # check insert
    flip = 0
    
    for i in hash1:
        if i not in hash2:
            flip += 1
    
    if (flip == 1):
        return True

    return False

    
strings = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'),
           ('pale', 'bake'), ('pale', 'pale')]

for i in strings:
    print(oneAway(i[0], i[1]))