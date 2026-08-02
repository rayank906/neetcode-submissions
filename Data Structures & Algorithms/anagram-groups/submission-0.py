class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            
        
        

           
            
        


"""
    1. make a hash table with keys as array of present letters a-z and value as a list of words with that combo
    2. return values of the hashmap
"""