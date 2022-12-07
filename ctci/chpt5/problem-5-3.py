# Flip a bit

#for i in bin(1775)[2:]:
#    print(i)

#print(stringed, x)

def bitFlipBrute(bittify):
    largest = 0
    for i in range(len(bin(bittify)[2:])):
        starter = bin(bittify)[2:]
        current = 0
        flip = 0
        for j in starter[int(i):]:
#            print(starter[int(i):])
            if int(j) == 0:
                flip += 1
            if flip > 1:
                break
            if int(j) == 0 and flip == 1:
                current += 1    

            if int(j) == 1:
                current += 1
#            print(j, current)
        if current > largest:
            largest = current
    print(largest)
    return largest

bitFlipBrute(1775)