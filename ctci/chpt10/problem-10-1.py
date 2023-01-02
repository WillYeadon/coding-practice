a = [1,2,3,5,6,8]
b = [4,7,9]

def sortedMerge(a, b):
    ans = []
    maxA = max(a)   
    maxB = max(b)   
    
    while (len(a) > 0) or (len(b) > 0):
        if len(a) > 0:
            can_a = a[0]
        else:
            can_a = maxA + 10
        if len(b) > 0:
            can_b = b[0]
        else:
            can_b = maxB + 10

        if can_a < can_b:
            ans.append(a.pop(0))
        else:
            ans.append(b.pop(0))

    return ans

print(sortedMerge(a, b))