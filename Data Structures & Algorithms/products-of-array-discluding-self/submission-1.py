class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        # compute prefix
        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        # compute postfix
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output

"""
    prefix sum variation.
    1. compute prefix and put it in input
    2. compute postfix and multiple in input array
    3. return output
"""
        