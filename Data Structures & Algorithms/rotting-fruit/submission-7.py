class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
            - count all fresh fruit in a set / store rotten on a queue
            - perform a BFS and pollute all fresh nearby
            - incr minutes
            - return minutes if fresh set empty if not -1

            TC: O(m*n)
            SC: O(m*n)
        """
        q = deque()
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        minute = 0
        while fresh and q:
            for i in range(len(q)):
                row, col = q.popleft()
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for ar, ac in neighbors:
                    r = row + ar
                    c = col + ac
                    if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 2 or grid[r][c] == 0:
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))
            minute += 1
        return minute if fresh == 0 else -1
                    
        
        
        