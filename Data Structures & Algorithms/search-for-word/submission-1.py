class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, curWord):
            if "".join(curWord) == word:
                return True
            if len(curWord) >= len(word):
                return False
            if r >= rows or c >= cols or r < 0 or c < 0 or (r, c) in visit:
                return False
            
            curWord.append(board[r][c])
            visit.add((r, c))

            if dfs(r + 1, c, curWord):
                return True
            if dfs(r - 1, c, curWord):
                return True
            if dfs(r, c + 1, curWord):
                return True
            if dfs(r, c - 1, curWord):
                return True
            
            curWord.pop()
            visit.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, []):
                        return True
        return False

"""
    1. loop through every row and column
    2. if an element is equal to the first letter, perform a dfs
    3. dfs explores r + 1, c - 1, c + 1, r - 1, checking for subsequent letter
    DFS Helper
        a. base case, if curWord = word, return True
        b. if len(curWord) >= len(word), return False
        b2. if r, c are oob or in visit, return False
        c. curWord += board[r][c]
        c2. add board[r][c] to visit
        d. if dfs(r+1), return True
        e. if dfs(r-1), return True
        f. if dfs(c-1), return True
        g. if dfs(c+1), return True
        h. curWord.pop()
        h2. remove from visit
        i. return False
    4. if dfs returns True, return True
    5. keep looping
    6. return False
"""
        