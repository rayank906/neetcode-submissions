class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            1. make nums a maxHeap
            2. pop k times from maxHeap to get kth largest

            TC: O(n) + O(klogn)
            SC: O(n)
        """
        heapq.heapify_max(nums)
        for _ in range(k):
            res = heapq.heappop_max(nums)
        return res
        