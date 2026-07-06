class KthLargest:
    def percolateDown(self, i):
        """
            a. while a left child exists
            b. if out of order, swap with smaller child
            c. else break
        """
        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[i] and self.heap[2 * i + 1] < self.heap[2 * i]:
                temp = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = self.heap[i]
                self.heap[i] = temp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                temp = self.heap[2 * i]
                self.heap[2 * i] = self.heap[i]
                self.heap[i] = temp
                i = 2 * i
            else:
                break
    
    def percolateUp(self, i):
        while i > 1 and self.heap[i // 2] > self.heap[i]:
            temp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = temp
            i = i // 2

    def __init__(self, k: int, nums: List[int]):
        """
            1. init a min heap
                a. find first elem w children, assign to cur
                b. while cur > 0
                c. percolate
                f. move to cur - 1
            2. pop n - k times
                a. override root with last element
                b. percolate
            TC: O(n) + O((n-k)logn)
        """
        if nums:
            nums.append(nums[0])
        self.heap = nums
        self.k = k
        cur = (len(self.heap) - 1) // 2
        # build heap
        while cur > 0:
            i = cur
            self.percolateDown(i)
            cur -= 1
        # pop until size k
        for _ in range(len(self.heap) - 1 - k):
            self.heap[1] = self.heap[len(self.heap) - 1]
            self.heap.pop()
            i = 1
            self.percolateDown(i)

    def add(self, val: int) -> int:
        """
            1. append value to heap
            2. pop only if minheap len > k
            3. return top value
            TC: O(logn) + O(1)
        """
        if not self.heap:
            self.heap.append(-1)
        self.heap.append(val)
        self.percolateUp(len(self.heap) - 1)
        if len(self.heap) - 1 > self.k:
            self.heap[1] = self.heap[len(self.heap) - 1]
            self.heap.pop()
            i = 1
            self.percolateDown(i)
        return self.heap[1]



        
