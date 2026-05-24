class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # get the dimensions:
        ROWS, COLS = len(matrix), len(matrix[0])

        # iterate through all ROWS:
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:  # target is greater than the greatest value in that row
                top = row + 1  # move top pointer
            elif target < matrix[row][0]:  # target is less than the smallest value in that row
                bot = row - 1  # move bot pointer
            else:  # found the row containing target possibly!
                break
        
        if not (top <= bot):  # confirm above loop ran, else return False
            return False
        
        # iterate through COLS now:
        l , r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1  # target is big, then we want our matrix number to be bigger too!
            elif target < matrix[row][m]:  # target is smaller will make our matrix number small as well
                r = m - 1
            else:
                return True
        return False