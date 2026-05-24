class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Get the number of rows and colums
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Go through every row and every column
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:  # if we ever find any value thats 0:
                    matrix[0][c] = 0  # we set in the first row, in that particular column the value 0
                    if r > 0:
                        matrix[r][0] = 0  # if the above condition is met, we also wanna set to 0 in that row and at the very first column
                    else:
                        rowZero = True  # otherwise we set our rowZero boolean to True

        # Go through every single position one more time and check if they're 0. We have to miss the 1st row and 1st col as we will handle that later  
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # check if origin of our matrix is 0
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0  # zeroing out the first column of our matrix
            
        if rowZero:  # meaning if it is True -- We will have to zero out the first row
            for c in range(COLS):
                matrix[0][c] = 0
        
