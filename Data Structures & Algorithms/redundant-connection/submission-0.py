class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            - union find for edges
            - when calling union, if fails, add to res array
            - return res[len(res) - 1]
        """
        parent = {}
        rank = {}
        res = []

        for i in range(1, len(edges) + 1):
            parent[i] = i
            rank[i] = 0
        
        def find(n):
            i = n
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p2] < rank[p1]:
                parent[p2] = p1
            else:
                parent[p2] = p1
                rank[p1] += 1
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                res.append([e1, e2])
        return res[len(res) - 1]
        