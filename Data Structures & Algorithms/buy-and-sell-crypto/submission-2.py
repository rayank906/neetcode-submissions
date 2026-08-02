class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            max profit: buy lowest and sell future highest
            1. l, r init to first position
            1b. init profit to 0
            2. move r
                a. if r <= l, l = r, r += 1
                b. else, profit = max(profit, curProfit)
            3. return profit
        """
        l, profit = 0, 0
        for r in range(1, len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                curProfit = prices[r] - prices[l]
                profit = max(profit, curProfit)
        return profit
        