class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [-1 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
            if res[i] == -1:
                res[i] = 0
        return res

"""
    for every element, loop through the rest of the array
    1. make res of len(temperatures) w "null" values -1
    2. for first elem, loop through entire array and stop as soon as greater temp found out.
    3. put j - i at the pos in res
    4. if pos == -1, change to 0
"""
        