class Solution:
    def isValid(self, s: str) -> bool:
        """
            0. make hashmap of close to open
            1. add open brackets to the stack
            2. when encounter closed brackets,
                3. if stack empty or last elem != closetoopen[c], 
                    return false
            4. return true if stack empty
        """
        stack = []
        bracketMap = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        for c in s:
            if c in bracketMap:
                if not stack or stack[-1] != bracketMap[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return True if not stack else False
        