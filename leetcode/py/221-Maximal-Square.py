class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side

class SlowSolution:
    def check(self, slider, matrix):
        h = len(matrix)
        w = len(matrix[0])

        x_range = w - slider
        y_range = h - slider
        found = False
        for x in range(x_range + 1):
            if found: break
            for y in range(y_range + 1):
                if found: break
                skip = False
                h_slice = matrix[y:y+slider]        
                for r in h_slice:
                    if skip: break
                    for c in r[x:x+slider]:
                        if skip: break
                        if c == '0': skip = True
                if not skip: found = True
        return found

    def maximalSquare(self, matrix):
        ans = 0
        shortest = min(len(matrix), len(matrix[0]))
        # check atleast 1
        checker = False
        for i in range(len(matrix[0])):
            if checker: break
            for j in range(len(matrix)):
                if checker: break
                if matrix[j][i] == '1':
                    checker = True
                    break
        if not checker: return 0
        # 1D special case
        if shortest == 1:
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    if matrix[j][i] == '1':
                        return 1
            return 0
        i = 0
        while i < shortest:
            i += 1
            slider = i
            check = self.check(slider, matrix)
            if check: 
                ans = i
            else:
                i = shortest + 10
        return pow(ans, 2)