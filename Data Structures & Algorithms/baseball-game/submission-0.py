class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if op == "C":
                res.pop()
            elif op == "D":
                res.append(2 * res[-1])
            elif op == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        return sum(res)
    
"""
    is +, C, D alone possible?
    1. use a stack to keep track of the result
    3. for D, pop the stack and double its value, then push
    4. for C, pop the stack
    5. for +, access the last two elements and push their sum
    6. for int, push to stack

    Edge cases:
     
    TC, SC: O(n), O(n) space  
"""
        