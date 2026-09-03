class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            brute force:
                - grab total
                - recursively try every subset
                - stop when total - sum subset = sum subset
            O(2^n)
            optimal:
                - cache subsets with state dp = num, total 
        """
        totalNum = sum(nums)
        if totalNum % 2 != 0:
            return False
        target = totalNum // 2
        dp = {}
        def dfs(i, currTotal):
            if (i, currTotal) in dp:
                return dp[(i, currTotal)]
            if target == currTotal:
                return True
            if i >= len(nums) or currTotal > target:
                return False
            res = dfs(i + 1, currTotal + nums[i]) or dfs(i + 1, currTotal)
            dp[(i, currTotal)] = res
            return res
        return dfs(0, 0)
        
        