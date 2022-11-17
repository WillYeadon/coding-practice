import copy

matrix = [[1,2,3,6],
          [2,2,0,4],
          [3,8,3,4],
          [9,4,7,4],
          [1,1,1,1]]

def zeroMatrix(matrix):
    ans = copy.deepcopy(matrix)
    N = len(matrix[0])
    M = len(matrix)
    
    zero_i = -1
    zero_j = -1

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                zero_i, zero_j = i, j
                print("hit", (i, j))
                for k in range(M):
                    for l in range(N):
                        if k == zero_i or l == zero_j:
                            ans[k][l] = 0
                zero_i, zero_j = -1, -1

    for i in range(len(ans)):
        print(ans[i])

zeroMatrix(matrix)