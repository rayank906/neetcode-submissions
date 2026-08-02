class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmt = 0
        currAmt = 0
        l, r = 0, len(heights) - 1
        while l < r and l < len(heights) and r > 0:
            currAmt = (r - l) * min(heights[l], heights[r])
            maxAmt = max(currAmt, maxAmt)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxAmt




"""
    2ptr: O(n^2) sol
        1. create max var
        2. for each elem, loop through all other elements
        3. calculate amt of water held, if >max update max
            b. subtract 2ptrs for distance and * w/ min(p1, p2)
        4. return max
    
    Edge cases:
        1. same elem: algo handles
"""     