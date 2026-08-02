class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pairs

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea
            


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

    stack approach
    1. use a stack to hold idxs and values
    2. idxs will be starts for their rectangles, not curr idx
    3. push idx, when encountered smaller value, pop until top of stack <= val
    4. 
"""
        