class Solution:
    def climbStairs(self, n: int) -> int:
        """
            - init arr of size 2 = [1, 1]
            - loop through n - 1 times
            - calc total = sum of arr values
            - arr[1] = arr[0]
            - arr[0] = total
            - return arr[0]
        """
        if n <= 1:
            return 1
        dp = [1, 1]
        for i in range(n-1):
            total = dp[0] + dp[1]
            dp[1] = dp[0]
            dp[0] = total
        return dp[0]
            

        