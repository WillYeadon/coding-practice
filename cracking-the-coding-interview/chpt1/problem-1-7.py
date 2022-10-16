# rotate a N,N matrix 90 degrees
# step here is that you have to recognize this is a transpose and mirror
# I assumed no numpy as otherwise np.rot90() solves instantly

matrix = [[1,2,3,6],
          [2,2,7,4],
          [3,8,3,4],
          [9,4,4,4]]

def rot90(matrix):
    
    N = len(matrix)
    temp = 0
    
    # create transpose
    for i in range(N):
        for j in range(i, N, 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
          
    # swap columns
    for i in range(N):
        # this will leave once j condition fails
        for j, k in zip(range(N // 2), range(N - 1, 0, - 1)):
#            print(i, j, k)
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][k]
            matrix[i][k] = temp

    for i in range(len(matrix)):
        print(matrix[i])

rot90(matrix)    
