class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curSet = [], []
        total = 0
        def helper(i, curSet, total):
            if total == target:
                combs.append(curSet[:])
                return
            if total > target or i >= len(nums):
                return
            
            # append nums[i]
            curSet.append(nums[i])
            total += nums[i]
            helper(i, curSet, total)

            curSet.pop()
            total -= nums[i]

            # explore without nums[i]
            helper(i + 1, curSet, total)
        
        helper(0, curSet, total)
        return combs

"""
    1. create a res array, total variable, currSet array
    2. call our helper with nums, currSet, res, total
        a. if total == target, append copy of curSet to res and return
        b. if total > target, return
        c. 
    3. return combs
"""
        