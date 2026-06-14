class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            1. if opening and closing == n:
                append to res, return
            2. if closing < opening,
                add a closing
                recurse
                pop closing
            3. if opening < n, 
                add a opening
                recurse
                pop opening
            4. call helper on res
            5. return res
        """
        def recurse(openingNum, closingNum, curr, res):
            if openingNum == n and closingNum == n:
                res.append("".join(curr))
                return
            
            if openingNum > closingNum:
                curr.append(")")
                recurse(openingNum, closingNum + 1, curr, res)
                curr.pop()
            
            if openingNum < n:
                curr.append("(")
                recurse(openingNum + 1, closingNum, curr, res)
                curr.pop()
        
        res = []
        recurse(0, 0, [], res)
        return res
        
