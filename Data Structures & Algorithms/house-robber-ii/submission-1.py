class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            - make a house robber helper,
            - run it without last and without first
            - init dp arr of two elems
            - loop through elems from n-2
            - at any given i,
                - rob i and go to i+2
                - skip i and go to i+1
            - return max(dp)
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0, 0]
        first, last = 0, 0
        for i in range(0, n-1):
            curr = max(nums[i] + dp[1], dp[0])
            dp[1] = dp[0]
            dp[0] = curr
        first = max(dp)
        
        dp = [0, 0]
        for i in range(1, n):
            curr = max(nums[i] + dp[1], dp[0])
            dp[1] = dp[0]
            dp[0] = curr
        last = max(dp)
        return max(first, last)
        