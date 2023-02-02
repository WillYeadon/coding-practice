def bitSwap(x):    
    # Gonna have to manipulate as string
    orig = bin(x).split('0b')[1][::-1]
    if (len(orig) % 2) == 1:
        orig += '0'
    
    odds = ''
    evens = ''
    
    for i in range(0,len(orig), 2):
        evens += orig[i]
    
    for i in range(1, len(orig), 2):
        odds += orig[i]
    
    output = ''
    for i, j in zip(odds, evens):
        output += i
        output += j
        
    
    return '0b' + output[::-1]

a = 25
b = 40
c = 100

print(bin(a), bitSwap(a))
print(bin(b), bitSwap(b))
print(bin(c), bitSwap(c))