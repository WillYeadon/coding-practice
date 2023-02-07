from random import randint

# Origional array
x = [1,3,5,8,9,10,14,15,18,22,30,36,41,50]
x = sorted(x)
orig = x

# Rotate by random amount
ran = randint(1, len(x))
x = x[ran:] + x[:ran]
#print(orig)
print(x)

def builtInFindN(x, N):
    if N not in x:
        print(N, 'is not in the array')
        return 
    
    print(N, 'is at index', x.index(N))
    
builtInFindN(x, 3)
builtInFindN(x, 7)

def search(arr, target):
    # initialize the start and end indices
    left, right = 0, len(arr) - 1
    
    # perform binary search
    while left <= right:
        # calculate the middle index
        mid = (left + right) // 2
        
        # check if the middle element is equal to the target
        if arr[mid] == target:
            return mid
        
        # if the right side of the array is sorted
        elif arr[mid] < arr[right]:
            # check if the target is present in the right side
            if target > arr[mid] and target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        # if the left side of the array is sorted
        else:
            # check if the target is present in the left side
            if target >= arr[left] and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    
    # return -1 if the target is not found
    return -1

print(search(x, 3))