class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image
        
        rows, cols = len(image), len(image[0])
        visit = set()

        def dfs(r, c, original):
            if (r >= rows or c >= cols or 
                r < 0 or c < 0 or
                (r, c) in visit or
                image[r][c] != original):
                return
            
            image[r][c] = color
            visit.add((r, c))
            dfs(r + 1, c, original)
            dfs(r - 1, c, original)
            dfs(r, c + 1, original)
            dfs(r, c - 1, original)
        
        original = image[sr][sc]
        dfs(sr, sc, original)

        return image

"""
    1. go to sr, sc, if color == curr color, return image
    2. save the orig color, change to color
    3. dfs helper on r+1, c+1, c-1, r-1 with original
    DFS Helper
        a. if r,c oob or r,c in visit return
        b. if curr color != orig, return
        c. change its color, dfs on all adjacent nodes
    4. return image
"""
        