class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            r = i + 1
            while r < len(prices):
                profit = max(prices[r] - prices[i], profit)
                r += 1
        return profit

"""
    1. for each element, calculate profit with all next elements
    2. if > curr profit, replace curr_profit
    3. return curr profit

    Edge cases:
        - no profit, handled in code
        - multiple max profits, thats fine
"""