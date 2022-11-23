def printBinary(number):
    # Special case of number out of range
    if number <= 0 or number >= 1:
        print('Number out of 0-1 range')
        return
    
    pre = '0 1000 0000 '
    ans = ''
    
    ans = pre
    if len(pre) > 32:
        print('Error')
    else:
        print(ans)
    
printBinary(0.5)