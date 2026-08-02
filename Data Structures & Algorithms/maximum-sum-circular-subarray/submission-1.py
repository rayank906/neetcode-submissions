class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum, maxSum = nums[0], nums[0]
        curMin, curMax = 0, 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            curMin = min(curMin, 0)
            curMax = max(curMax, 0)
            curMin += nums[i]
            curMax += nums[i]
            minSum = min(curMin, minSum)
            maxSum = max(curMax, maxSum)
        return max(total - minSum, maxSum) if maxSum > 0 else maxSum
        

"""
    1. loop through all elements
    2. keep track of maxSum, minSum, currMax, currMin, total
    3. return max(total - minSum, maxSum)
"""
        