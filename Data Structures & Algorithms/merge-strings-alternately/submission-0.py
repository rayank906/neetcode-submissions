class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        res = ""
        while w1 < len(word1) and w2 < len(word2):
            res += word1[w1]
            res += word2[w2]
            w1 += 1
            w2 += 1
        
        if w1 < len(word1):
            while w1 < len(word1):
                res += word1[w1]
                w1 += 1
        elif w2 < len(word2):
            while w2 < len(word2):
                res += word2[w2]
                w2 += 1
        return res
    
    """
        1. two pointers to the start of both arrays
        2. while both are valid, append them alternatively
        3. when one goes oob, check if the other has chars left, and append all of them

        EC:
            if single character, while will catch
    """
        