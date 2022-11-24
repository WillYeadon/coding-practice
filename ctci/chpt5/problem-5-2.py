def helperSplit(number):
    x = str(number).split('.')
    return x[0], x[1]

def helperStick(number, value):
    x = str(value) + '.' + str(number)
    return float(x)

def printBinary(number):
    # Special case of number out of range
    if number <= 0 or number >= 1:
        print('Number out of 0-1 range')
        return
    
    startlength = len(str(number)) - 1
    split = helperSplit(number)
    stick = helperStick(split[1], 0)
    
    print(split, stick, startlength)
    
    pre = '0 1000 0000 '
    post = ''
    processed = number    
    
    while len(post) < 24:
        overall = helperSplit(processed)
        post += overall[0]
        
        mantissa = 2 * int(overall[1])
        if len(str(mantissa)) < startlength:
            processed = helperStick(mantissa, 0)
#            print('under', processed)
        else:
            processed = mantissa / 10**(startlength - 1)
#            print('over', processed, int(mantissa), 10**(startlength - 2))

    ans = pre + post
    # 32 bit plus spaces to print better
    if len(ans) > 36:
        print('Error', ans)
    else:
        print(ans)
    
printBinary(0.5)
