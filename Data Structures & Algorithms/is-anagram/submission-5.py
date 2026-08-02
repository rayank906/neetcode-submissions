class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            0. check s and t length
            1. make a freq map for s and t
            2. return whether or not freq maps are equal
        """
        if len(s) != len(t):
            return False
        
        freqS = {}
        freqT = {}

        for c in s:
            if c not in freqS:
                freqS[c] = 1
            else:
                freqS[c] += 1
        
        for c in t:
            if c not in freqT:
                freqT[c] = 1
            else:
                freqT[c] += 1
        
        return freqS == freqT
        