class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            - init dp array w last two values
            - loop from n-3 down to 0
                - cost from curr = cost + min of dp arr
            - return min of dp array
        """
        n = len(cost)
        dp = [cost[n - 2], cost[n - 1]]
        for i in range(n-3, -1, -1):
            curr_cost = cost[i] + min(dp)
            dp[1] = dp[0]
            dp[0] = curr_cost
        return min(dp)
        