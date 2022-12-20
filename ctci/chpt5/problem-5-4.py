def smallLargest(n):
    starter = bin(n)[2:]
    
    smaller = [i for i in starter]
    firstZero = -1
    seen = False
    
    for i in range(len(starter)):
        if (starter[i] == '0') and not seen:
            seen = True
            firstZero = i
    
    if firstZero == -1:
        return 'No zero!'
    
    flipped = False
    for i in range(firstZero, -1, -1):
        if (smaller[i] == '1') and not flipped:
            smaller[i] = '0' 
            flipped = True
    
    for i in range(len(smaller)):       
        if i == firstZero:
            smaller[i] = '1'
    
    larger = [i for i in starter]
    nextOne = -1
    seen = False
    
    for i in range(firstZero, len(starter)):
        if (starter[i] == '1') and not seen:
            seen = True
            nextOne = i
    
    if nextOne != -1:
        pass
    else:
        oneCount = 0
        for i in larger:
            if i == '1':
                oneCount += 1
        for i in range(len(larger)):
            larger[i] = '0'
        larger.append('0')
        for i in range(len(larger) - 1, len(larger) - 1 - oneCount, -1):
            larger[i] = '1'
        larger[0] = '1'
    
    ansSmall = ''
    for i in smaller:
        ansSmall += i
        
    ansLarge = ''
    for i in larger:
        ansLarge += i
    
    a = '0b' + ansLarge
    b = '0b' + ansSmall
    
    return (bin(n),a,b, nextOne)

print(smallLargest(56))

