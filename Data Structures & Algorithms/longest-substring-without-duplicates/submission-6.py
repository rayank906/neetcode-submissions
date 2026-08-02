class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = 0
        seen = set()
        while r < len(s) and l < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = max(length, len(seen))
            r += 1
        return length

        
    
"""
    1. init l, r = 0, 0, init seen set
    2. move r forward
    3. if char in seen,
        empty seen set
        update length to len(seen)
        move l forward until != curr char
        assign r to l
    4. return length

    Edge cases:
        1. empty string: wouldnt loop and would return 0
        2. single element string: loop once, update length, ret 1
"""