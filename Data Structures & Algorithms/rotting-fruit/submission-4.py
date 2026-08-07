class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, minutes = 0, 0
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    curr_r = r + dr
                    curr_c = c + dc
                    if (curr_r < 0 or curr_r >= rows or
                        curr_c < 0 or curr_c >= cols or
                        grid[curr_r][curr_c] != 1):
                        continue
                    grid[curr_r][curr_c] = 2
                    queue.append([curr_r, curr_c])
                    fresh -= 1
            minutes += 1

        if fresh != 0:
            return -1
        return minutes



"""
    1. first pass, count num of fresh fruits, append rotten fruits
    to queue
    2. init minute counter
    3. while queue, for every element on the queue
    3b. pop from the q and make the fruit rotten
    4. loop through neighbours, if == 1, make rotten and add to queue
    5. incr minute count
    6. return minute if fresh == 0 fruits else -1

    TimeC: O(m * n)
    SpaceC: O(m * n)
"""
        