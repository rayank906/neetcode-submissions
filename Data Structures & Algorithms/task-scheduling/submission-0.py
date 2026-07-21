class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            1. get counts of each element
            2. keep track of most frequent in max heap
                a. heapify arr of counts
            3. use a cooling queue to store elements processed
            4. while maxheap or q non empty
            5. if maxheap non empty, pop, append [count, time to pop] to q
            6. incr time
            7. add idle if neither maxheap nor q available
        """
        counts =  Counter(tasks)
        maxHeap = [count for count in counts.values()]
        coolQ = deque()
        
        heapq.heapify_max(maxHeap)
        time = 0
        while maxHeap or coolQ:
            time += 1

            if maxHeap:
                task = heapq.heappop_max(maxHeap)
                task -= 1
                if task > 0:
                    coolQ.append([task, time + n])
            if coolQ and coolQ[0][1] == time:
                task = coolQ.popleft()
                heapq.heappush_max(maxHeap, task[0])

        return time



        