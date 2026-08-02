class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

    
"""
    1. find the curr longest substring [with its indexes]
        a. use a char
        b. keep track of curr len, max len, maxl, maxr
        c. init l to 0, loop through s with r
        d. if s[r] != char, char = s[r], l = r, max[s] update, currlen = 0
        e. curr len += 1
    2. using k, figure out by how much we can extend s
        a. since we have indexes, check if left of maxL and right of maxR are valid
        b. if both are, we can extend by 2
        c. if only 1 is, we can extend by 1, else no extend
    3. return len(curr longest) + extend amount

    TC, SC: O(n), O(1)

    EC:
        single char string: maxLen will be 1, extend will be 0, returns 1
        empty char string: loop never runs, extend and maxLen stay 0 so 0 returns
"""
        