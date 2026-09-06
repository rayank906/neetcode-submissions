class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            - init adj list from 1 to n node: [w, e]
            - init min heap
            - add node k to min heap
            - while heap, 
                - pop curr node, add it to hashmap
                - add all neighbors to heap
            - return max of values of hashmap if hashmap len == n
        """
        adj = {i: [] for i in range(1, n+1)}
        for src, dest, weight in times:
            adj[src].append([weight, dest])
        minHeap = []
        minHeap.append([0, k])
        heapq.heapify(minHeap)
        shortest = {}

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = weight
            for neighW, neigh in adj[node]:
                if neigh not in shortest:
                    heapq.heappush(minHeap, [neighW + weight, neigh])
        return max(shortest.values()) if len(shortest) == n else -1
        