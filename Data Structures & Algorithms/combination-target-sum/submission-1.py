class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            total += nums[i]
            helper(i, cur, total)
            cur.pop()
            total -= nums[i]

            helper(i + 1, cur, total)
        
        helper(0, [], 0)
        return res

"""
    1. make a res array
    2. make helper, [i, cur, total]
        a. Base cases
            i. if total == target, append to res and return
            ii. if total > target or i >= len(nums), return
        b. append element at i to cur
        c. call helper with i to explore all combs with elem i
        d. pop elem i
        e. call helper with i + 1 to explore all combs without element i
    3. call helper
    4. return res

    TimeC: O(2^t/m)
    SpaceC: O(t/m)
"""
        