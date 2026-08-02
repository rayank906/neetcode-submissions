class Solution:
    def helper(self, i, nums, curSet, res):
        if i == len(nums):
            res.append(curSet[:])
            return

        # Explore with nums[i]
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, res)
        curSet.pop()

        # Explore without nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, curSet, res)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, curSet = [], []
        self.helper(0, nums, curSet, res)
        return res

"""
    1. use a backtracking with helper func
    1b. sort the input array so duplicates are next to each other
    2. helper function starting idx, nums, curSet, res
        3. if i == len(nums):
            append copy curSet to res
            return
        4. append nums[i] to curSet
            a. recursively explore subsets with nums[i]
            pop nums[i]
            hop over all duplicates
            b. explore all subsets without nums[i]
    5. return res

    TimeC: O(n * 2^n)
    SpaceC: O(n)
"""
        