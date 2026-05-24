class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the dimensions of the matrixc
        ROW, COL = len(matrix), len(matrix[0])

        # iterate through the rows to find the row that contains target value
        top, bot = 0, ROW - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:  # target is greater than the greatest value in that row
                top = row + 1  # move top row down one unit
            elif target < matrix[row][0]:  # target is less than the smallest value in that row
                bot = row - 1  # move bottom row up by one unit
            else:  # we possibly found the row containing target!
                break
        
        if not (top <= bot):  # in case above while loop has ran but we didnt find target value in any row
            return False

        row = (top + bot) // 2
        l, r = 0, COL - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:  # found the target!
                return True
        
        return False  # if above while loop didnt return True by this point meaning target is not present in matrix
