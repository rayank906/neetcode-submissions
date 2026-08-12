class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            - build adj list
            - loop for path using dfs, if cycle found, return []
            - if visited, auto return True
            - dfs on all prereqs
            - add node to output and mark visited
            - run a dfs on all nodes and return res
        """
        graph = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        path = set()
        visit = set()
        res = []

        def dfs(course):
            if course in path:
                return False
            if course in visit:
                return True
            
            path.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visit.add(course)
            res.append(course)
            return True
        
        for course in graph:
            if not dfs(course):
                return []
        return res
        