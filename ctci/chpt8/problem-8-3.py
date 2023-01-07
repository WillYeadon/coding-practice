# Magic index
A = [-5,-3,-2,1,2,3,6]
B = [-3,-1,0,2,5,5,5]

def magic(a):
    for i in a:
        if i == a[i]:
            return True, i

def magicRec(a):
    x = a.pop(-1)
    if len(a) > 0:
        if x == len(a):
            y = True, x
        else:
            y = magicRec(a)
        return y
    else:
        return False

print(magic(A))
print(magic(B))
print(magicRec(A))
print(magicRec(B))