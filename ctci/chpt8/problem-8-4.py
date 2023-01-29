# Powerset, return all subsets of a set
# Recusion candidate!

def powerset(cand):
    # There are 2^n subsets for a set of size n

    # Base case for the empty set
    if len(cand) < 1:
        return [[set()]]
    
    # Takes the end one off
    popped = cand.pop()

    # Recursive
    sets = powerset(cand)

    # For each element (list) in the lsit 
    # 'sets' it will add the list [popped]
    subsets = []   
    for i in sets:
        subsets.append(i + [popped])

    # Return is the origion sets and these
    # new subsets
    return sets + subsets

a = set([1,1,2,2,3,4])
b = set([432,1325,213])
c = set([1,2])

#print(powerset(a))
#print(powerset(b))
print(powerset(c))