class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 2
        numHash = {}
        for n in nums:
            if n in numHash:
                numHash[n] += 1
            else:
                numHash[n] = 1
            if numHash[n] >= maj:
                    return n
             

"""
    1. make majority = n/2
    2. make hashmap of nums and count
    3. when freq == majority, return that number
"""
        