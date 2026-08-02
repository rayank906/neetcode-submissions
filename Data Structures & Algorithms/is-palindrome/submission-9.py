class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            1. init l, r to front and back of s
            2. while l <= r:
            3. while l < len(s) and !l.isalnum(), l += 1
            4. while r > 0 and !r.isalnum(), r -= 1
            4b. if l >= len(s) or r <= 0, break
            5. if l.lower() != r.lower(), return false
            6. l += 1, r -= 1
            7. return true
        """
        
        l, r = 0, len(s) - 1
        while l <= r and l < len(s) and r > 0:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > 0 and not s[r].isalnum():
                r -= 1
            if l >= len(s) or r <= 0:
                break
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        