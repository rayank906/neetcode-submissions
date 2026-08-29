class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            - if 1 elem, return element
            - init dp arr of 2
            - at any i:
                - rob i and add dp[1]
                - take dp[0]
            - return max(dp)
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0, 0]
        for i in range(n):
            temp = max(nums[i] + dp[1], dp[0])
            dp[1] = dp[0]
            dp[0] = temp
        return max(dp)
        
