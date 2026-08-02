class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            1. init res to arr of l and r ptrs, reslen to inf
            2. if len t > len s, return ""
            3. init l, r to 0
            4. init freqMap for window and pop freqMap for t
            5. init have to 0, need to len(freqMap of t)
            6. while r < len(s)
            7. update window w current char
            8. if count of c in window == count in t, incr have
            9. if have == need, update minS, move l
            10. if window count for c < count in t, decr have
            11. return s[l:r + 1] if resLen changed
        """
        minS = [-1, -1]
        minLen = float("infinity")
        if t == "":
            return ""
        
        l, r = 0, 0
        tMap, window = {}, {}
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        have, need = 0, len(tMap)

        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in tMap and window[s[r]] == tMap[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < minLen:
                    minS = [l, r]
                    minLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = minS[0], minS[1]
        return s[l:r + 1] if minLen != float("infinity") else ""
