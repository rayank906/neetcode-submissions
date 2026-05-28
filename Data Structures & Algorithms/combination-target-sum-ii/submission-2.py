class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            Helper takes in curr position, currCombs, total
                1. base case: if total >= target, if equal append, return
                2. choose an element and append to currComb
                3. loop through all possible next choices and recurse on the helper    
        """
        combs, currComb = [], []
        total = 0
        candidates.sort()
        
        def helper(i, currComb, total):
            if total >= target or i >= len(candidates):
                if total == target:
                    combs.append(currComb.copy())
                return

            currComb.append(candidates[i])
            total += candidates[i]
            helper(i + 1, currComb, total)
            currComb.pop()
            total -= candidates[i]
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            helper(i + 1, currComb, total)
        
        helper(0, currComb, total)
        return combs
        