class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                top = stack.pop()
                res[top[0]] = i - top[0]
            stack.append([i, v])
        return res

"""
   1. make a stack of def value zero
   2. when elem encountered, push it.
   3. keep track of idx of top
   4. when elem encountered > top, pop top and modify res, else push and update top_idx
"""
        