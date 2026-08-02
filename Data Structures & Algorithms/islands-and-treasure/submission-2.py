class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visit.add((r, c))
        
        def add(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visit or 
                grid[r][c] == -1):
                return

            queue.append([r, c])
            visit.add((r, c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist

                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1       

        

"""
    1. grab rows and cols
    2. make visit set
    3. NUANCE: Add all treasures to the queue and to visit
    3b. init dist to 0
    4. starts BFS (while queue)
    5. loop through q
    6. pop from q and assign grid[r][c] to dist (originally zero so doesnt affect treasures)
    7. add all + 1 neighbours to the queue and to visit
    8. after loop, increment dist to 1 (at the next it, all nodes dist 1 from a gate (no matter which one)
    will be assigned to 1)

    TC: O(m * n)
    SC: O(m * n)
"""
        