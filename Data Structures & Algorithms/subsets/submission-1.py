class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            1. make a global subset arr
            2. make a helper that takes idx, arr, curr, global subset
                a. add to currset
                b. recurse in helper with element
                c. pop from curset
                d. recurse without element
                e. stop if idx >= len(nums)
                f. add curset copy to global subset
            3. init curset and subsets
            4. call helper
            5. return subsets
        """
        def helper(i, nums, curr, subsets):
            if i >= len(nums):
                subsets.append(curr.copy())
                return
            
            curr.append(nums[i])
            helper(i + 1, nums, curr, subsets)
            
            curr.pop()
            helper(i + 1, nums, curr, subsets)
            return
        
        subsets, curr = [], []
        helper(0, nums, curr, subsets)
        return subsets