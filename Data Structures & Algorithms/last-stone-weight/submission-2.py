class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
            0. init a max heap with stones
            1. while len(stone) > 1
            2. pop y and x from the heap
            3. if x < y,
            4. push y-x into the heap
            5. return stones[0] if stones else 0

            TimeC: O(nlogn)
        """
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x < y:
                heapq.heappush_max(stones, y-x)
        return stones[0] if stones else 0
        


        