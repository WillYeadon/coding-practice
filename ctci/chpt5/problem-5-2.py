def helperSplit(number):
    x = str(number).split('.')
    return x[0], x[1]

def helperStick(number):
    x = str(0) + '.' + str(number)
    return float(x)

def printBinary(number):
    # Special case of number out of range
    if number <= 0 or number >= 1:
        print('Number out of 0-1 range')
        return
    
    startlength = len(str(number)) - 1
    pre = '0 1000 0000 ' # Sign plus exponent bits
    post = '' # 23 digit mantissa
    processed = number    
   
    while len(post) < 24:
        # This will be fed in a float of either 0.XXX or 1.YYY
        # Takes the first bit and sticks onto post 
        overall = helperSplit(processed)
        post += overall[0]

        # Double mantissa and it is either greater than one
        # in which case can just proceed or it is still '0.'
        # which needs adding back on (sorry for poor expl)        
        mantissa = 2 * int(overall[1])
        if len(str(mantissa)) < startlength:
            processed = helperStick(mantissa)
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
