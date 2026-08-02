class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            1. init l,r, longest, cur to 0
            2. init seen set
            3. while r < len(s)
                4. if r in seen
                    update longest to max longest curr
                5. while r in seen: 
                    seen.remove(l)
                    incr l
                    decr curr
                6. add r to seen
                7. incr r
                8. incr curr
            9. return longest
        """
        l, r = 0, 0
        longest, curr = 0, 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                longest = max(curr, longest)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                    curr -= 1
            seen.add(s[r])
            r += 1
            curr += 1
        return max(longest, curr)
        