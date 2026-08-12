class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            - build adj list of nodes
            - perform dfs using visit set. If a node was seen,
            cycle must exist so impossible return false
        """
        graph = {}
        for course, pre in prerequisites:
            if course not in graph:
                graph[course] = []
            if pre not in graph:
                graph[pre] = []
            graph[course].append(pre)
        
        visit = set()
        def dfs(course):
            if not graph[course]:
                return True
            visit.add(course)
            for pre in graph[course]:
                if pre in visit:
                    return False
                if not dfs(pre):
                    return False
            visit.remove(course)
            graph[course] = []
            return True
        
        for course in graph:
            if not dfs(course):
                return False
        return True


        