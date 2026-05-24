class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l (buying) will start from index 0 and right pointer (selling) from next to left ie index 1.
        maxProfit = 0  # make sure to initialize the variables you will use in your loops. (especially while loop)
        while r < len(prices):  # starting our while loop, and we will keep iterating while our right pointer has not crossed the length of prices.
            # transaction profitable or not?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r  # in case transaction is not profitable, we bring l to r and then we will move r to right by 1 to move on to the next index.
            r += 1  # so no matter what, right pointer will move to the right and in case there is no profit, we brought l to the same index as the right poiner r.
        
        return maxProfit  # once the while loop ends, we return maxProfit as we know that this was the variable updating on each iteration to contain the maximum profit.

"""Confirm if starting/bounds of while loop are set differently here with sliding
window than the regular two pointer implementation."""