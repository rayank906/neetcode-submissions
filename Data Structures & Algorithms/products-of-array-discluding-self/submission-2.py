class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= product
            product *= nums[i]
        
        return prefix

"""
    1. loop forward and make a prefix array
        a. init product to 1
        b. keep track of curr product
        c. multiply after updating prefix array
    2. loop in reverse to make a suffix array
        a. perform same ops
    3. loop through prefix, multiply elems with suffix
    4. return prefix array

    TimeC: O(n)
    SpaceC: O(n)

    Edge cases:
        a. neg numbers
        b. empty array? [np]
"""