class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # have two pointers from each end, keep multiplying them
        # save the max result in a variable that we later return 

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, curr_area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:  # deosnt matter we can move any pointer, once above while loop condition isnt being met it will terminate
                l += 1
        return max_area