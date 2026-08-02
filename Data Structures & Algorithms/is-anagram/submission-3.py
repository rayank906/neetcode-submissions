class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        

'''
    1. loop through characters in s
    2. if char not in t, return false
    3. return true in the outer loop
    SC: O(1), no additional memory used
    TC: O(n + m), for every character, loop at most m times to find the character

    EGDE C:
        contains different number of same character
        xx and x, bccc and cbbb
'''       