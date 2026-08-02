class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        rows, cols = len(grid), len(grid[0])
        maxCount = 0

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or (r, c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count = dfs(row, col)
                    maxCount = max(count, maxCount)
        
        return maxCount

"""
    0. make a visit set
    1. Loop through the grid
    2. When we encounter a 1, perform a dfs to count the number of 1s
    in that island
        DFS helper
        a. If curr node is 0 or r, c OOB or r,c in visit, return
        b. add r,c to visit set
        c. return 1 + dfs of r + 1, r - 1, c + 1, c - 1
    3. update maxCount of the island with count returned by dfs
    4. return maxCount

    TimeC: O(m * n)
    SpaceC: O(m * n)
"""
        