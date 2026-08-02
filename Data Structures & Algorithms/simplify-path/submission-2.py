class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        stack = []
        i = 1
        while i < len(path):
            if path[i] != '/':
                while i < len(path) and path[i] != '/':
                    curr += path[i] 
                    i += 1 
                if curr == '..':
                    stack.pop() if stack else None
                elif curr == '.':
                    continue
                else:
                    stack.append(curr)
            curr = ""
            i += 1
        return '/' + '/'.join(stack)     


"""
    Unix-style:
        a. single dot: ignore
        b. double periods: pop previous directory
        c. multiple slashes reduce to single
        d. >2 periods: directory name
    
    1. use a stack
    2. do not add slashes to stack, only content
    3. if not slash, while not slash, append everything to curr
    4. see what curr is after that while loop and decide accordingly
    5. '/'+'/'.join(stack)
    5. return stack
"""
        