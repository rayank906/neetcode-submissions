class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        brute: 
            for every word, check if it exists in s
            O(n^2*m)
         optimal:
            - create dp array of len s
            - dp[i] = is word break from here to the end possible
            - dp[len(s)] = True
            - at every i from the back, check if we can get any word in the dict
            - if we can assign true, if not assign false
            O(n^2)
        """
        dp = {len(s): True}
        for i in range(len(s) - 1, -1, -1):
            dp[i] = False
            for w in wordDict:
                if s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
        