class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)  # number of rows in the matrix. Matrix is a 2-D matrix and in that case the length of the matrix is its number of rows.
        n = len(matrix[0])  # number of columns in the matrix. Matrix[0] refers to the first row of the matrix. and len(matrix[0]) returns number of columns in the matrix as matrix is assumed to be well-formed (all rows have the same number of columns), len(matrix[0]) gives the number of columns in any row of the matrix.

        for  i in range(m):  # iterating through the rows.
            for j in range(n):  # for that row, iterating through columns.
                if matrix[i][j] ==  target:  # matrix[i][j] accesses the element in the i-th row and j-th column of the matrix.
                    return True
                else: pass  # this line is optional.
        return False  # if both for loops end it means that no match found hence we return False OUTSIDE both for loops.
        









"""This is the brute force method with time complexity O(m*n)"""