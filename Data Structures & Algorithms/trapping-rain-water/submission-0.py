class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(1, len(height) - 1):
            trap = min(max(height[:i]), max(height[i:])) - height[i]
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
        