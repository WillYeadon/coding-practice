# Recursive multiplier without using *

def recursiveMult(x, y):
    if y <= 0:
        return 0
    else:
        return x + recursiveMult(x, y - 1)

print(recursiveMult(5, 5))
print(recursiveMult(6, 7))
print(recursiveMult(3, 10))