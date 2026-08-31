class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
            Brute:
                - try all subarray sums and return the maximum product
            O(n^2)
            
            Optimal:
                - keep track of max and min
                    dp = [max, min]
                - at each step:
                    - save max and reset if num is 0
                    - multiply value by max and min maximum and update
                    - return res
        """
        n = len(nums)
        dp = [1, 1]
        res = max(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                dp[0], dp[1] = 1, 1
                continue
            prod_1 = dp[0] * nums[i]
            prod_2 = dp[1] * nums[i]
            dp[0] = max(prod_1, prod_2, nums[i])
            dp[1] = min(prod_1, prod_2, nums[i])
            res = max(res, dp[0])
        return res

        