class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0 for i in range(len(height))]
        maxR = [0 for i in range(len(height))]
        minLR = [0 for i in range(len(height))]

        # calc maxL
        seenMax = height[0]
        for i in range(1, len(maxL) - 1):
            maxL[i] = seenMax
            if height[i] > seenMax:
                seenMax = height[i]
        
        # calc minL
        seenMax = height[len(height) - 1]
        for i in range(len(maxR) - 2, -1, -1):
            maxR[i] = seenMax
            if height[i] > seenMax:
                seenMax = height[i]
        
        for i in range(1, len(minLR) - 1):
            minLR[i] = min(maxL[i], maxR[i])
        
        area = 0
        print(minLR, maxL, maxR)
        for i in range(1, len(minLR) - 1):
            trap = minLR[i] - height[i]
            area += trap if trap > 0 else 0
        return area


"""
    min(l, r) - h[i] is eqn used to trap water for every i
    min(max[:i],max[i:])

    1. loop through every element from 1, len(height) - 1
    2a. trap = min(max[:i], max[i:]) - height[i]
    2. area += trap if trap > 0 else 0 
    3. return area
"""
        