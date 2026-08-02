class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        def palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        while l < r:
            if s[l] != s[r]:
                return palindrome(s[l+1:r+1]) or palindrome(s[l:r])
            l += 1
            r -= 1
        return True
                

"""
    use two pointers front and back
    1. l, r = 0 , n-1
    2. move l and r and check for equality while l < r
    3. if l != r, move l and check if equal to r
        if not, move back and do same for r
    4. if both operations fail, return false
    5. else continue the loop
    6. return true outside
"""
        