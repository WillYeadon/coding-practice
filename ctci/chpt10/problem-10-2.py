# Sort this list so that anos are together. 
# Should be alphabetically order anagrams
# first then remainder
anos = ['pass', 'loop', 'aged', 'pool', 'care',
        'mite', 'post', 'pale', 'peal', 'cake',
        'rake', 'emit', 'race', 'item', 'deck',
        'hoop', 'plea', 'bake', 'beak', 'time',
        'leap', 'sire', 'list', 'seal', 'liar']

# Helper that finds whether perm of not
def isPermutation(a, b):
    return set(a) == set(b)

def sortWithAn(can):
    # Initial sort and overall lengeth for loop
    alph = sorted(can)
    words = len(alph)

    # Declar lists for use later
    ans = [] # Answer list to be returned
    added = [] # List of index of anas found
    remainder = [] # Whatever is left
       
    while True:
        # Stops last iter
        if len(alph) > 0:
            # New candidate is the first item
            candidate = alph[0]
        subAns = []
        # Will exit while loop at end
        flag = False

        # Loop through the remainder of the list
        for i in range(len(alph)):
            # If perm set flag to true
            if isPermutation(alph[i], candidate) and (alph[i] != candidate):
                flag = True
                # Add candidate to sub ans
                if candidate not in subAns:
                    added = []
                    subAns.append(candidate) 
                # also add ana to sub ans
                subAns.append(alph[i])
                # Record the index of anas
                added.append(i)
#                print('Match found! Now on', subAns)

        # Pop from end
        added.sort(reverse=True)
        for i in added:
            # Loop through a remove anas
            alph.pop(i)
        # Refresh added to zero for next run
        added = []

        # If found ana then add the collection
        # To the answer
        if flag and (len(subAns) > 0):
            subAns.sort()
            for i in subAns:
                ans.append(i)
            subAns = []
        # Elsewise reduce length of origional list
        elif words > 0:
            if len(alph) > 0:
                remainder.append(alph.pop(0))
            words -= 1
        # Last loop no flag or anything left
        # Add on remained words to ans
        else:
            if len(remainder) > 0:
                for i in remainder:
                    ans.append(i)
            break
    
    return ans

print(sortWithAn(anos))
