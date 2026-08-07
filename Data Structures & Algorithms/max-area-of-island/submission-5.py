class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
            1. when 1 encountered, count how large island is
                - use a dfs helper
                    a. if node oob or visited, return 0
                    b. visit all neighbors, return count
            2. as we count, change 1s to 0s
            3. check if curr count > global count
            4. return count
        """
        ROW, COL = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r, c + 1) + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    count = max(dfs(r, c), count)
        
        return count

        