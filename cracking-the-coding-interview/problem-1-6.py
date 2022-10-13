# String compression aabcccccaaa to a2b1c5a3

def stringCompression(string):
    ans = ""
    count = 0
    unique = ""
    
    for idx, i in enumerate(string):
        if unique != "": # for first run through
            if i != unique: # moving onto a new letter
                ans += (unique + str(count))
                count = 1
                unique = i
                if idx == (len(string) - 1): # exit at end
                    ans += (unique + str(count))
                continue
        if i == unique:
            count += 1 # same letter so increment
            if idx == (len(string) - 1): # exit at end
                ans += (unique + str(count))
        else:
            unique = i # have a new letter not at string end
            count += 1
    
    return ans
            

strings = ['aabcccccaaa', 'aaabbbcccd', 'abcabc', 'aabbccdd']

for i in strings:
    print(stringCompression(i))