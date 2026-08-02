class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect, min_seen = 0, heights[0]
        for l in range(len(heights)):
            min_seen = heights[l]
            for r in range(l, len(heights)):
                min_seen = min(heights[r], min_seen)
                area = (r - l + 1) * min_seen
                max_rect = max(max_rect, area)
        return max_rect


"""
    brute force approach
    1. l, r to first bar
    2. w = l - r + 1
    3. for every element, use r to go through all possible rectangles
        keep track of max rectangle seen
    4. keep track of min_seen and calc max rectangle using w * min_seen
    5. return max rectangle

    TC: O(n^2)
    SC: O(1)
"""
        