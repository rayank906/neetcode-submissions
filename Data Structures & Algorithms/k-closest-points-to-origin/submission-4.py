class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
            1. for every point,
            2. calc euclidean distance
            3. insert dist at the start
            4. heapify points
            5. pop k times to get k closest elements and append to res
            6. return res

            TC: O(klogn) on avg, worst case nlogn
            SC: O(n)
        """
        res = []

        for p in points:
            dist = (p[0]) ** 2 + (p[1]) ** 2
            p.insert(0, dist)
        
        heapq.heapify(points)
        
        for _ in range(k):
            x = heapq.heappop(points)
            res.append([x[1], x[2]])
        
        return res
        