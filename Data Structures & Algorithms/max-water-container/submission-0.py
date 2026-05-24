class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0  # initialize the res as area must be 0 at the beginning cant be negative.
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r - l) * min(heights[l], heights[r])  # whichever one is the smaller value that will be the bottleneck ie decide the area.
                res = max(res, area)  # this makes sure that res always holds the maximum res value at the end of each iteration. We give it res's old and value and new area computed and res then becomes the bigger value of the two.

        return res
        