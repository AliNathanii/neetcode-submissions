class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the dimensions of our matrix.
        ROWS, COLS = len(matrix), len(matrix[0])

        # two pointers for our rows now. Top and bottom. Top row is 0 and bottom row is rows - 1 as if lets says rows are 15 so last row will be indexed at 14.
        top, bot = 0, ROWS - 1 
        while top <= bot:  # starting binary search until we can find the target row or declare that its not in there.
            row = (top + bot) // 2  # target row at each iteration will be the middle one ie calculated like this.
            if target > matrix[row][-1]:  # case 1: target value is greater than the Greatest Value in that row. syntsx for that is matrix[row][-1] as it will give us last item in that row which in a sorted row will be the largest value.
                top = row + 1  # shift the top pointer down.
            elif target < matrix[row][0]:  # case 2: if target value is less than the smallest number in current mid row, this case we:
                bot = row - 1  # we shfit the bottom pointer up.
            else:  # we are already / or finally are in the row where target value is, in that case we:
                break  # break out of this while loop.
        
        if not (top <= bot):  # if we have been through the above while loop and didnt find the row where target value is there, simply return False. This is the syntax to see that above while loop has ended and we didnt find any row with our target value.
            return False
        
        # now we will move on the second binary search of the code.
        # this binary search will be run on the current row that we found from the while loop above.
        # this is why here we declare row value OUTSIDE the while loop, using the latest bot and top value we found as the while loop above ended.
        row = (top + bot) // 2
        l, r = 0, COLS - 1  # r pointer is sett to the right most column. l pointer to the very first column indexed at 0.
        while l <= r:  # condition for this while loop, ie we always use pointers as the conditions of while loop.
            m = (l + r) // 2  # computing the middle point in that row.
            if target > matrix[row][m]:  # if target value is greater than the value in this target row at position m ie matrix[row][m]
                l = m + 1  # that means we have to search towards the right of the middle row! So we move the left pointer towards right.
            elif target < matrix[row][m]:  # if target value is less than the value in matrix at [row] and column [m] 
                r = m - 1  # in this case we wanna search towards the left so we move right pointer towards left hence we subtract 1 from it.
            else:  # we found the target value!
                return True
        return False  # loop has ended and we never found the target, so we return False after/outside the loop.
