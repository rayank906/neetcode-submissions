class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify_max(self.maxHeap)
        

    def addNum(self, num: int) -> None:
        """
            1. add to maxHeap
            2. if root of max > root of min, send root of max to min
            3. if min size - 1 > max size, pop min root, add to max

            TC: O(log n)
        """
        
        heapq.heappush_max(self.maxHeap, num)
        if self.minHeap and self.maxHeap[0] > self.minHeap[0]:
            elem = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, elem)

        if len(self.minHeap) - 1 > len(self.maxHeap):
            elem = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, elem)
        if len(self.maxHeap) - 1 > len(self.minHeap):
            elem = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, elem)
        

    def findMedian(self) -> float:
        # TC: O(1)
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        return (self.minHeap[0] + self.maxHeap[0]) / 2
        
        