class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r >= rows or c >= cols or
                r < 0 or c < 0 or grid[r][c] == 0):
                return 1
            
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))
            
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)

"""
    1. loop through every row and col
    2. once we find a one, perform dfs to count the number of 
    edges of the squares
    DFS HELPER
        a. if r, c oob or grid(r, c) equal 0, return 1 because its a boundary
        b. if in visit, return 0 bc not boundary
    3. return dfs(r, c)

    TimeC: O(k) where k is the size of the island
    SpaceC: O(k)
"""
        