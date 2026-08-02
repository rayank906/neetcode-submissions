class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        n = len(nums)
        for i in range(n):
            j = i
            while j < i + n:
                curSum = max(curSum, 0)
                curSum += nums[j % n]
                maxSum = max(curSum, maxSum)
                j += 1
            curSum = 0
        return maxSum

"""
    for every element, while idx < i + n:
        1. keep track of curSum, maxSum
        2. before adding to curSum, if curSum < 0, reassign to 0
        3. add to curSum, update maxSum if necessary
        4. return maxSum
"""
        