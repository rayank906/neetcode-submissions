class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l], profit)
            else:
                l = r
            r += 1
        return profit
"""
    1. set l, r to first and second elem
    2. for every elem, if r < l, set l to r
    3. else calculate profit and update profit if necessary
"""