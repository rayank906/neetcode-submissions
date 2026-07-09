class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            1. init min heap
            2. add num to minheap
            3. pop when size of minheap > k
            4. return root of minheap

            TC: O(nlogk)
            SC: O(k)
        """
        minHeap = []
        heapq.heapify(minHeap)
        
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
        