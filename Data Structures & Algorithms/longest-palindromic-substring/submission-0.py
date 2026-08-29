class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            - for every characters
                - start with two ptrs at the char
                - while both inbound and char eq
                    - check if len grt than max, sav idx at max
                    - expand out
                - repeat with ptr i, i+1 to capture even len pal
                - return arr[maxl:maxr]
        """
        maxL, maxR = 0, 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (maxR - maxL + 1):
                    maxL, maxR = l, r
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (maxR - maxL + 1):
                    maxL, maxR = l, r
                l -= 1
                r += 1
        return s[maxL:maxR+1]