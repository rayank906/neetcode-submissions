class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            Helper takes in curr position, currCombs, total
                1. base case: if total >= target, if equal append, return
                2. init prev to None
                3. loop through all possible choices at that level
                    if prev == curr element, skip it
                4. update prev as we loop 
        """
        combs, currComb = [], []
        total = 0
        candidates.sort()
        
        def helper(i, currComb, total):
            if total >= target or i >= len(candidates):
                if total == target:
                    combs.append(currComb.copy())
                return
            prev = None
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                currComb.append(candidates[j])
                total += candidates[j]
                helper(j + 1, currComb, total)
                currComb.pop()
                total -= candidates[j]
                prev = candidates[j]
        
        helper(0, currComb, total)
        return combs
        