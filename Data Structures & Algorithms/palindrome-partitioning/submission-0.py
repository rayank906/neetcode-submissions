class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            1. make a palindrome helper function
            2. init res array
            3. make partition helper
            PARTITIONS Helper
                a. if i >= len(s), append curPart to res
                b. loop through i and len(s), if partion is palindrome
                append to part and explore other partitions in the remaining str
            PALINDROME Helper
                a. l, r = 0, len(input) - 1
                b. while l <= r,
                c. if char at l != char r, return False
                d. return True
        """
        res = []
        part = []

        def palindrome(s_in, l, r):
            while l <= r:
                if s_in[l] != s_in[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def partitions(i):
            if i >= len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if palindrome(s, i, j):
                    part.append(s[i:j + 1])
                    partitions(j + 1)
                    part.pop()

        partitions(0)
        return res
        