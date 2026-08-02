class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitMap = {}
        digitMap['2'] = ['a', 'b', 'c']
        digitMap['3'] = ['d', 'e', 'f']
        digitMap['4'] = ['g', 'h', 'i']
        digitMap['5'] = ['j', 'k', 'l']
        digitMap['6'] = ['m', 'n', 'o']
        digitMap['7'] = ['p', 'q', 'r', 's']
        digitMap['8'] = ['t', 'u', 'v']
        digitMap['9'] = ['w', 'x', 'y', 'z']

        def backtrack(i, curSet):
            if i >= len(digits):
                res.append("".join(curSet[:]))
                return
            
            for char in digitMap[digits[i]]:
                curSet.append(char)
                backtrack(i + 1, curSet)
                curSet.pop()
        
        backtrack(0, [])
        return res

"""
    1. make a hashmap of num to letters
    2. init a curset and res
    HELPER [traversal using i]
        3. if i >= len(digits), append copy of curset to res
        4. for char in hashmap[i], append to cur and explore with i + 1
        5. pop after exploring
    6. init call with 0, [], res
    7. return res
"""
        