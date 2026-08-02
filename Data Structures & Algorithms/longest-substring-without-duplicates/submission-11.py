class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            1. init set to hold substr
            2. init l, r to 0
            3. while r < len:
                a. if r not in set, add r to set, incr r
                b. else, save len to max
                    while r in set, remove l and incr l
            4. return max
        """
        window = set()
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
            else:
                maxLen = max(maxLen, len(window))
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
        maxLen = max(maxLen, len(window))
        return maxLen