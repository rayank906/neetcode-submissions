class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= rows or c >= cols or 
            r < 0 or c < 0 or 
            (r, c) in visit or i >= len(word) or 
            board[r][c] != word[i]):
                return False
            
            visit.add((r, c))

            if (dfs(r + 1, c, i + 1) or 
            dfs(r - 1, c, i + 1) or 
            dfs(r, c + 1, i + 1) or 
            dfs(r, c - 1, i + 1)):
                return True
            
            visit.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

"""
    1. loop through every row and column
    2. perform a dfs
    3. dfs explores r + 1, c - 1, c + 1, r - 1, checking for subsequent letter
    DFS Helper
        a. base case, if i == len(word), return True
        b. if i >= len(word), return False
        b2. if r, c are oob or in visit or board[r][c] != word[i], return False
        c. add board[r][c] to visit
        d. if dfs(r+1), return True
        e. if dfs(r-1), return True
        f. if dfs(c-1), return True
        g. if dfs(c+1), return True
        h2. remove (r, c) from visit
        i. return False
    4. if dfs returns True, return True
    5. keep looping
    6. return False

    TimeC: O(n * m * 4^w) because we go through the whole grid (n * m)
            and we have 4 calls to dfs for every dfs
    SpaceC: O(n)
"""
        