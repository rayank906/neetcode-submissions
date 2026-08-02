class Solution:
    def helper(self, i, nums, curSet, res):
        if i == len(nums):
            res.append(curSet[:])
            return
        
        # Explore subsets with element i
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, res)
        curSet.pop()

        # Explore subsets without i
        self.helper(i + 1, nums, curSet, res)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curSet = [], []
        self.helper(0, nums, curSet, res)
        return res

"""
    1. make a helper function to traverse all possible subsets
    2. helper function takes in starting idx, nums, curr, res
        3. if i == len(nums), append curr to the res
        4. append element at i to currset
            a. Explore subsets with element i
            Recursive call to helper function with i + 1
        5. Explore subsets without element i
            pop from curset, then make recursive call
    6. return res array

    TimeC: O(n * 2^n)
    SpaceC: O(n) for the recursive call stack
"""
        