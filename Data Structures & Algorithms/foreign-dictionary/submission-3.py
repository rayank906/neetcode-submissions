class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
            - take two words at a time
            - loop through both words until a letter differs
            - when a letter differs
                - add a directed edge in adjacency list
            - dfs on adj list
            - add node to res when dfs returns
            - reverse the resulting list

            incorrect ordering cases:
                - cycle in graph (z, o, z)
        """
        
        # build adj list
        adj = {c: [] for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            p1, p2 = 0, 0
            while p1 < len(w1) and p2 < len(w2):
                if w1[p1] != w2[p2]:
                    adj[w1[p1]].append(w2[p2])
                    break
                p1 += 1
                p2 += 1
        
        # run topo sort on adj list to find ordering
        def dfs(node, visit, path):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            visit.add(node)
            for neigh in adj[node]:
                if not dfs(neigh, visit, path):
                    return False
            topSort.append(node)
            path.remove(node)
            return True
        
        topSort, visit, path = [], set(), set()
        for node in adj:
            if not dfs(node, visit, path):
                return ""
        topSort.reverse()
        return "".join(topSort)