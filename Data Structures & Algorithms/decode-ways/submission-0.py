class Solution:
    def numDecodings(self, s: str) -> int:
        """
            - init a cache with len(s) = 1
            - base case:
                - i in dp:
                    return dp[i]
                - i contains zero / invalid, return 0
            - incr res with dfs(i+1)
            - incr w dfs(i+2) only if i+1 and double digit <= 26
            - cache res in dp
            - return res
        """
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and int(s[i:i+2]) <= int(26):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
        