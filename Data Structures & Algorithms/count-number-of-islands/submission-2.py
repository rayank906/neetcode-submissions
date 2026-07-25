class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
           1. loop through the grid with r, c
           2. change all seen 1s to 0s
           3. increment numIsl only if everything surrounding is seen / water 
           
           TimeC: O(m * n)
           Space: O(m * n)
        """
        count = 0
        row = len(grid)
        col = len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0" # mark seen                   
            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count
        