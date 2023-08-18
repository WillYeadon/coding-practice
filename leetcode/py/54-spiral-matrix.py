class Solution:
    def popOutside(self, matrix):
        ans = []
        
        # 1. Process the top row:
        # Pop the first row from the matrix.
        # Since pop(0) returns the first row as a list, 
        # we extend 'ans' with this list to add all its elements.
        ans.extend(matrix.pop(0))
        
        # 2. Process the rightmost column:
        # Check if there are any rows left in the matrix after popping the top row
        if matrix:
            # For each row in the matrix except the last one, pop the last element (rightmost column) 
            # and append it to 'ans'.
            for row in matrix[:-1]:
                if row:
                    ans.append(row.pop())

            # 3. Process the bottom row:
            # If there are rows left after processing the rightmost column, 
            # pop the last row from the matrix, reverse it and extend 'ans' with it.
            if matrix:
                ans.extend(matrix.pop()[::-1])

            # 4. Process the leftmost column:
            # After processing the bottom row, if there are still rows left, 
            # for each of these rows, pop the first element (leftmost column) and append it to 'ans'.
            if matrix:
                for row in matrix[::-1]:  # We iterate over the remaining rows in reverse order.
                    if row:
                        ans.append(row.pop(0))
        
        # Return the elements in the outer spiral layer as a list.
        return ans

    def spiralOrder(self, matrix):
        ans = []
        
        # While there are rows left in the matrix, pop the outer layer 
        # and add its elements to the 'ans' list.
        while matrix:
            ans.extend(self.popOutside(matrix))

        # Return the final spiral order list.
        return ans
