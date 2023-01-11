# Bit flip req

def convert(x, y):
    if x == y:
        print(0)
        return

    a = x if (x > y) else y
    b = y if (x > y) else x
    
    A = str(bin(a))
    B = str(bin(b))
    
    A = A.split('b')[-1]
    B = B.split('b')[-1]
    
    while len(B) < len(A):
        B = '0' + B     
    
    bits = 0
    
    for i in range(len(A)):
        if A[i] != B[i]:
            bits += 1
    
    print(bits, A, B)


convert(29,15)