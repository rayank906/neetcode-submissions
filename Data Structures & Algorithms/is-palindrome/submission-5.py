class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < len(s) and r >= 0 and (l < r)):
            while l < r and (not s[l].isalnum()):
                l += 1
            while l < r and (not s[r].isalnum()):
                r -= 1
            if (s[l].lower() != s[r].lower()):
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
        