class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        stack = []
        for i, v in enumerate(position):
            stack.append([v, i])

        stack.sort(key=lambda item:item[0])

        top = stack.pop()
        steps = (target - top[0]) / speed[top[1]]

        for i in range(len(position) - 2, -1, -1):
            curr = (target - stack[i][0]) / speed[stack[i][1]]
            if curr <= steps:
                stack.pop()
                continue
            else:
                count += 1
                top = stack.pop()
                steps = (target - top[0]) / speed[top[1]]
        return count + 1
            

"""
    1. put pos and idx in stack
    2. sort stack and loop in reverse
    3. have a count. take value, calculate steps to reach end
    4. for the next element, calculate steps to reach end
        i. if steps >= prev elem steps, move to next and check
        ii. else, append count, reset steps to next elem
    5. return count

    **catch: fleet moves at speed of top element

"""     