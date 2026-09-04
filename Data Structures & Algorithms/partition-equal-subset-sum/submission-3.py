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
            O(n * target)
        """
        totalNum = sum(nums)
        if totalNum % 2 != 0:
            return False
        target = totalNum // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            temp = set()
            for j in dp:
                temp.add(j + nums[i])
            dp.update(temp)
        return (target in dp)
        
        