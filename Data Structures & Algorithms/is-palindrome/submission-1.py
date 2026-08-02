class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        for c in s:
            if not c.isalnum():
                s = s.replace(c, "")
        l = 0
        r = len(s) - 1
        while (l < len(s) and r >= 0 and (l < r)):
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True



"""
    1. strip space and make all char lower
    2. use two pointers to go from front and back and compare every character
    3. incr/decr until l >= r or they go oob
    4. if l >= r, return true | else return false
"""
        