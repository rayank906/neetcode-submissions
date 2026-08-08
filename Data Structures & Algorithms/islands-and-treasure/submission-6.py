class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            0. start from treasure
            1. init a deque w 0,0
            2. pop elem off,
                - if land, assign len
            3. if oob, alr visited, -1 ignore
            4. add neighbor to queue
            5. add neighbor to visit set()
            6. incr length after all queue ops
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = pow(2, 31) - 1
        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
                    
        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == INF:
                    grid[r][c] = length
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for ar, ac in neighbors:
                    if r + ar < 0 or c + ac < 0 or r + ar >= ROWS or c + ac >= COLS or (r + ar, c + ac) in visit or grid[r + ar][c + ac] == -1 or grid[r + ar][c + ac] == 0:
                        continue
                    q.append((r + ar, c + ac))
                    visit.add((r + ar, c + ac))
            length += 1



        