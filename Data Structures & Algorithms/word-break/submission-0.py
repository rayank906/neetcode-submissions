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
        words = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            dp[i] = False
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    dp[i] = dp[j + 1]
                if dp[i]:
                    break
        return dp[0]
        