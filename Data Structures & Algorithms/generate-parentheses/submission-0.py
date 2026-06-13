class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            A. Generate paranthesis
                1. if opening and closing == 0,
                    if well formed, add to res
                    return
                2. if opening == 0, add closing and backtrack
                3. if closing == 0, add opening and backtrack
                4. add opening, backtrack
                5. pop
                6. add closing and backtrack
            B. Check if well formed
                takes in arr of paranthesis
                1. loop through the paranthesis
                2. if opening,
                    add opening on a stack
                3. if closing,
                    if stack is empty, return false
                    pop from opening stack
                4. if stack not empty, returnf false
                5. return true
        """
        def wellFormed(parantheses):
            openingStack = []
            for p in parantheses:
                if p == "(":
                    openingStack.append("(")
                else:
                    if not openingStack:
                        return False
                    openingStack.pop()
            if openingStack:
                return False
            return True
        
        def recurse(openingNum, closingNum, curr, res):
            if openingNum == 0 and closingNum == 0:
                if wellFormed(curr):
                    res.append("".join(curr))
                return
            
            if openingNum == 0:
                curr.append(")")
                recurse(openingNum, closingNum - 1, curr, res)
                curr.pop()
                return
            if closingNum == 0:
                curr.append("(")
                recurse(openingNum - 1, closingNum, curr, res)
                curr.pop()
                return
            
            curr.append(")")
            recurse(openingNum, closingNum - 1, curr, res)
            curr.pop()
            curr.append("(")
            recurse(openingNum - 1, closingNum, curr, res)
            curr.pop()
        
        res = []
        recurse(n, n, [], res)
        return res
        
