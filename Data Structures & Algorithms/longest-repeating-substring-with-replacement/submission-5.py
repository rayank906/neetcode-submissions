from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            1. init freqMap
            2. init l, r, longest to 0
            3. for given window,
            4. if r - l + 1 - maxcount <= k (num reps to be made)
            5. window valid, update longest
            6. else, slide l while r - l + 1 > k
            7. return longest
        """
        rep = k
        l, r, longest = 0, 0, 0
        freqMap = defaultdict(int)
        
        while r < len(s):
            freqMap[s[r]] += 1
            while (r - l + 1) - max(freqMap.values()) > k:
                freqMap[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest
            
        