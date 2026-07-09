class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            1. init a empty max heap, res
            2. for every point,
            3. calc euclidean distance
            4. add to heap if dist <= root heap dist or len(res) < k
            5. pop from heap if len heap > k
            6. return res
        """
        res = []
        heapq.heapify_max(res)

        for p in points:
            dist = (p[0] - 0) ** 2 + (p[1] - 0) ** 2
            p.insert(0, dist)
            if not res or dist <= res[0][0] or len(res) < k:
                heapq.heappush_max(res, p)
            if len(res) > k:
                heapq.heappop_max(res)
        
        for p in res:
            p.pop(0)
        
        return res
        