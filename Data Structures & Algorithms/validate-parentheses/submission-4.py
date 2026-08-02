class Solution:
    def isValid(self, s: str) -> bool:
        """
            1. add open brackets to the stack
            2. when encounter closed brackets, pop from stack
            3. if mismatch when popped, return false
            4. return true
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ')':
                    if stack[-1] != '(':
                        return False
                elif c == ']':
                    if stack[-1] != '[':
                        return False
                elif c == '}':
                    if stack[-1] != '{':
                        return False
                stack.pop()
        return True if not stack else False
        