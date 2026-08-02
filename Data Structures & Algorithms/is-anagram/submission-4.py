class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hash_s = {}
        for i in s:
            if i in hash_s:
                hash_s[i] += 1
            else:
                hash_s[i] = 1
        
        for j in t:
            if j in hash_s:
                hash_s[j] -= 1
        
        for key in hash_s:
            if hash_s[key] != 0:
                return False
        return True
        

'''
    1. create hashmap for s with counts of the occurences of each letter
    2. loop through t, decrease occurence of a letter as encountered
    3. loop through hashmap again and check if everyone is zero before returning true
    SC: O(1), no additional memory needed
    TC: O(2n + m) -> O(n + m)
'''       