class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(m * n) ie dimensions of matrix
        # O(1) memory complexity as we are not saving anything (if you dont count the output as extra memory)
        # O(n) if output is considered as extra memory
        
        res = []
        left, right = 0, len(matrix[0])  # right pointer is the number of columns + 1 ie the length of the matrix
        top, bottom = 0, len(matrix)  # bottom is the length of matrix which will tell us the number of rows

        while left < right and top < bottom:
            # get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])  # we know we are in the top row, and for column we can put i
            top += 1  # shift top, down by 1

            # get every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])  # row is i and column is right - 1 because we know that right is actually out of bounds
            right -= 1  # shift right pointer to left by 1

            if not (left < right and top < bottom):
                break  # break out of our while loop
            
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):  # left - 1 to include left
                res.append(matrix[bottom - 1][i])  # bottom - 1 for row as at this point we are at the bottom row and - 1 as bottom value would give out of bounds error. Column will be i as we are going from right to left
            bottom -= 1  # shift bottom pointer upwards

            # get every i in the left column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])  # row i and column will be the left most column
            left += 1  # shift left pointer to right by 1 unit
        
        return res



