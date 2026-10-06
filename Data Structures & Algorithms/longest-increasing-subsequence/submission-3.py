class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            brute: 
                - start at i=0
                - add elem i if > than prev (if sth in arr)
                - recurse without and return the max
                - once i == len(nums), return 0
            optimal:
                - from bottom, lis = max(lis[i], 1+lis[all the next])
        """
        lis = {i: 1 for i in range(len(nums))}
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])
        return max(lis.values())
        