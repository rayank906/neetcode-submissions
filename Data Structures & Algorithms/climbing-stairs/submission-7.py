class Solution:
    def climbStairs(self, n: int) -> int:
        """
            - start at 0
            - climb 1 step or 2 steps
            - if reach n, return 1
            - if above n, return 0
            - cache ways by adding counts
        """
        def ways(i, cache):
            if i == n:
                return 1
            if i > n:
                return 0
            if i not in cache:
                cache[i] = ways(i + 1, cache) + ways(i + 2, cache)
            return cache[i]
        return ways(0, {})
            

        