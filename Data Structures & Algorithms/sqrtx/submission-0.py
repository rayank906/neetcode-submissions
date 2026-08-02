class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid
        return r
"""
    binary search checking for squares
    1. l, r = 0, x
    2. calculate mid
    3. check if mid squared > x, r = mid - 1
    4. elif mid squared < x, r = mid + 1
    5. else, return mid
    6. return r
"""
        