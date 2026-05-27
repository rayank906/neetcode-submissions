class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            1. make a helper (takes i, sum, currComb, combs)
            2. base case: if sum >= target:
                if ==, add a copy to combinations
                return
            3. add nums[i]
            4. choose to recurse down that side with nums[i] (call helper with i)
            5. remove num[i]
            6. call helper with i + 1 (skip nums[i])
        """
        combs, currComb = [], []
        total = 0

        def helper(i, total, currComb, combs):
            if total >= target or i >= len(nums):
                if total == target:
                    combs.append(currComb.copy())
                return
            # choose nums[i]
            total += nums[i]
            currComb.append(nums[i])
            helper(i, total, currComb, combs)

            # skip nums[i]
            total -= nums[i]
            currComb.pop()
            helper(i + 1, total, currComb, combs)
        
        helper(0, total, currComb, combs)
        return combs

        