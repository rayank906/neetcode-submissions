class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBanana = max(piles)
        mid = 0
        minbph = maxBanana
        l, r = 1, maxBanana
        while l <= r:
            mid = l + ((r - l) // 2)
            hours = 0
            for p in piles:
                hours += int(math.ceil(p / mid))
            if hours > h:
                l = mid + 1
            else:
                minbph = min(minbph, mid)
                r = mid - 1
        return minbph

"""
   search range: 1 - max(piles)
   perform a bs:
    1. calculate mid
    2. pass through array with mid to calculate total hours
        a. divide each num by mid, ceil, and add to hours variable
    3. compare with h
    4. if hours > h, l = mid + 1
    5. elif hours < h, r = mid - 1, minbph = min(mid, minbph)
    6. else, minbph = min(mid, minbph), r = mid - 1
    7. return minbph 

    TC: O(nlogm) where m is max(piles)
    SC: O(1)
"""
        