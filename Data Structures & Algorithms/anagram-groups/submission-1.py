from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            1. build freqMap arr, visited bool array
            2. loop freqMap arr
            3. for every non visited freqMap,
                4. check if equal with curr, 
                b. append to a temp and mark visited
                5. append temp to result arr
                6. empty temp
        """
        visited = [False] * len(strs)
        maps = []
        res= []
        for s in strs:
            freqMap = defaultdict(int)
            for c in s:
                freqMap[c] += 1
            maps.append(freqMap)
        print(visited)
        
        for i in range(len(maps)):
            if visited[i]:
                continue
            visited[i] = True
            temp = [strs[i]]
            for j in range(i + 1, len(maps)):
                if not visited[j]:
                    if maps[i] == maps[j]:
                        temp.append(strs[j])
                        visited[j] = True
            res.append(temp)
        return res
        