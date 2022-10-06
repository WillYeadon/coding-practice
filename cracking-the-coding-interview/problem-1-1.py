# Is unique, want algorithm that test whether string contains
# all unique characters.

def isUnique(string):
    # There are only 123 candidate characters so a string
    # longer than this isn't unique
    if len(string) > 128:
        return False
    
    hash = {}
    
    for i in string:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in hash:
        if hash[i] != 1:
            return False
        
    return True
      
strings = ['abcdefghij', 'Unique', 'Repeat Repeat']

for i in strings: 
    print(isUnique(i))    