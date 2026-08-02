class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmt = 0
        currAmt = 0
        for i in range(len(heights)):
            ptr = i + 1
            while ptr < len(heights):
                currAmt = (ptr - i) * min(heights[i], heights[ptr])
                if currAmt > maxAmt:
                    maxAmt = currAmt
                ptr += 1
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