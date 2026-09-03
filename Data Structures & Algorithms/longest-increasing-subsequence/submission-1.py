class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            brute: 
                - start at i=0
                - add elem i if > than prev (if sth in arr)
                - recurse without and return the max
                - once i == len(nums), return 0
        """
        dp = {}
        def dfs(i, j):
            if i >= len(nums):
                return 0
            lis = dfs(i+1, j)
            if j == -1 or (nums[j] < nums[i]):
                if i in dp:
                    return max(lis, dp[i])
                else:
                    lis_with = 1 + dfs(i+1, i)
                    dp[i] = lis_with
                    lis = max(lis, lis_with)
            return lis
            
        return dfs(0, -1)
        