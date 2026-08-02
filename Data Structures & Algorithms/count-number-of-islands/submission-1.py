class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        visit = set()
        island_count = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(columns) or (r, c) in visit or grid[r][c] == '0':
                return
            visit.add((r, c))

            neighbours = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for dr, dc in neighbours:
                row = r + dr
                col = c + dc
                dfs(row, col)
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r, c) not in visit:
                    dfs(r, c)
                    island_count += 1
        
        return island_count

"""
    1. if not grid, return 0
    2. grab row and columns
    3. make dfs function
        Base cases:
            a. If r or c OOB or grid[r][c] == 0, return
            c. If r, c has been visited, return
        i. add r, c to visited
        ii. traverse r + 1, c + 1, r - 1, c - 1
    4. for every vertex in grid, if equal to 1 and not in visited, perform dfs
    and increment island count
    5. return island count

    TimeC: O(m * n)
    SpaceC: O(m * n) where m is the number of rows and n is the number of columns
"""
        