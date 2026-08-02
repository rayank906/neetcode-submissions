class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot_count, minutes, num_fruits = 0, -1, 0
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        queue = deque()

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    num_fruits += 1
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visit.add((r, c))
        print(num_fruits)
        
        # everything is rotten
        if num_fruits <= 0:
            return 0
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rot_count += 1
                for dr, dc in neighbors:
                    curr_r = r + dr
                    curr_c = c + dc
                    if (curr_r < 0 or curr_r >= rows or
                        curr_c < 0 or curr_c >= cols or
                        (curr_r, curr_c) in visit or
                        grid[curr_r][curr_c] == 0):
                        continue
                    elif grid[curr_r][curr_c] == 2:
                        rot_count += 1
                        visit.add((curr_r,curr_c))
                        continue
                    else:
                        queue.append([curr_r, curr_c])
                        visit.add((curr_r,curr_c))
            minutes += 1
        
        if rot_count < num_fruits:
            return -1
        return minutes



"""
    1. first pass, count total number of fruits, append rotten fruits
    to queue (add to visit set)
    2. init minute counter
    3. while queue, for every element on the queue
    3b. pop from the q and make the fruit rotten, incr rot count
    4. loop through neighbours, if == 1, add to queue
    5. incr minute count
    6. return minute if rot_count == num fruits else -1
"""
        