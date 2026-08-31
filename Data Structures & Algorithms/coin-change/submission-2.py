class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            base cases:
                - if num exceeds amt, return inf
                - if == amt, return 0
            - add num to res and recurse
            - skip num and recurse
            - return min of both
        """
        dp = {}
        def dfs(i, amount, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            if curSum == amount:
                return 0
            if i >= len(coins) or curSum > amount:
                return float("inf")
            minCoins = min(1 + dfs(i, amount, curSum + coins[i]), dfs(i + 1, amount, curSum))
            dp[(i, curSum)] = minCoins
            return minCoins
        count = dfs(0, amount, 0)
        return count if count != float("inf") else -1
        