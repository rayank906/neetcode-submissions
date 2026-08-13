class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            - build adj list
            - do dfs on unseen nodes and add to seen set
            - loop through graph, incr count only after dfs
        """
        seen = set()
        count = 0
        graph = {i: [] for i in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neigh in graph[node]:
                dfs(neigh)
            return
        
        for node in graph:
            if node not in seen:
                dfs(node)
                count += 1
        return count
        