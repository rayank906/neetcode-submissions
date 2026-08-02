class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(idx, curSet, total, target):
            if total == target:
                res.append(curSet[:])
                return
            if total > target or idx >= len(candidates):
                return
            
            prev = None
            for i in range(idx, len(candidates)):
                if prev == candidates[i]:
                    continue
                
                curSet.append(candidates[i])
                total += candidates[i]
                prev = candidates[i]
                helper(i + 1, curSet, total, target)
                curSet.pop()
                total -= candidates[i]
        
        helper(0, [], 0, target)
        return res

"""
    1. make a res array
    2. make a helper to traverse all possible combs
        a. Base case:
            if total > target or idx >= len(nums), return
            if total == target, append cur array to res
        b. for all nums in the range idx to len(nums):
        c. append to cur and incr. total
        d. then call helper on idx + 1
    3. call helper
    4. return res

    TimeC: O(u * n)
    SpaceC: O(u * n) where u is number of unique combs and n is input size
"""        