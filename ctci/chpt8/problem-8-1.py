# For a number of stairs n, how many possible steps up
# can you take if you can hop 1,2 or 3 at a TimeoutError

def tripleStep(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
        
    return tripleStep(n - 1) + tripleStep(n - 2)\
        + tripleStep(n - 3)

print(tripleStep(0))
print(tripleStep(1))
print(tripleStep(5))
print(tripleStep(15))