class Solution:
    def climbStairs(self, n: int) -> int:
        """
            1. if n < 1, return n
            2. return climbStairs(n - 1) + climbStairs(n - 2)
        """
        def memo(n, cache):
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = memo(n - 1, cache) + memo(n - 2, cache)
            return cache[n]
        return memo(n, {})