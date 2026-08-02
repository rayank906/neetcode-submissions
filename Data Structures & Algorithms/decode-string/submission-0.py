class Solution:
    def decodeString(self, s: str) -> str:
        nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curr = ""
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1] in nums:
                    num = stack.pop() + num
                num = int(num)
                stack.append(num * curr)
        return ''.join(stack)
        

"""
    1. use a stack to hold the numbers
    2. loop until a number [use set of number chars]
    3. if sq bracket, loop and grab everything in sq bracket
        then add it stack[-1] number of times to res
    4. if number reached, loop until bracket reached then push to stack
"""