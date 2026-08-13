class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            - cycles not allowed
            - valid path between all nodes

            - build adj list
            - maintain a path set and dfs through all paths
            - if in a path a repeated node, return False

            - if a pass completed through adj list and not == n, not connecteed
        """
        graph = {i : [] for i in range(n)}
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
        
        path = set()
        def dfs(node, prev):
            if node in path:
                return False
            path.add(node)
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return True if len(path) == n else False
