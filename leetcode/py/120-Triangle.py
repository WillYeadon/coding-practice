class Solution:
    def minimumTotal(self, triangle):
        counts = triangle
        for i in range(len(counts)):
            row = counts[i]
            if len(row) == 1:
                pass
            else:
                row[0] += counts[i - 1][0]
                row[-1] += counts[i - 1][-1]
                if len(row) > 2:
                    for j in range(1, len(row) - 1):
                        row[j] += min(counts[i - 1][j], counts[i - 1][j - 1])            

        return min(counts[-1])