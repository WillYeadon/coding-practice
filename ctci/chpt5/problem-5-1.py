# Bit Insertion
def insert(x, y, i, j):
    # Want to clear the bits between i and j
    # of x and then put y in the gap, you can
    # assume that there is enough space
    
    # Place a 1 at positiion j
    ones_j = -1 << (j + 1)
    # This will make 0 everywhere apart
    # from i then -1 makes everything
    # left of i 1
    ones_i = (1 << i) - 1
    # Now have zeros between two ones
    extract = ones_j | ones_i
    extracted = x & extract
    print(bin(ones_j), bin(ones_i),bin(extract))
    print(bin(x), bin(extracted))
    
    # Shift inserted code i bits
    inserted = y << i
    print('Code to be inserted', bin(inserted))
    return extracted | inserted


x = 0b10000000000
y = 0b10011

print('Inserted', bin(insert(x, y, 2, 6)))
#print(x, y)
#print(x + y)
