class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0  # initializing result as 0 at the very beginning.
        l, r = 0, len(heights) - 1  # initializing our two pointers starting from the left and right.

        while l < r:
            area = (r - l) * min(heights[l], heights[r])  # going for the samller value as that will be the bottleneck that will decide the area.
            res = max(res, area)  # new res will be the larger value of the two values given as parameter of max()

            # now we will have to move the pointers, we move the pointers this way as this will get us the max area value.
            if heights[l] < heights[r]:
                l += 1  # if left is smaller number then we will move the left pointer to the right.
            elif heights[l] > heights[r]:
                r -= 1  # if r is smaller then we move right poiter to the left.
            else:  
                r -= 1  # if they are the same then it doesnt matter which one we move.
        return res
