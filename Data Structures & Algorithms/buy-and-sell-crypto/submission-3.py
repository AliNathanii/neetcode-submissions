class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0  # no need to initialize this
        maxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)  # l pointer is not to be moved here
            else:
                l = r
            r += 1
        return maxProfit