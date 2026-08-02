class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            1. make an arr of size 26
            2. loop through s and t
            3. increment arr[ord(c) - ord('a')] for s and decr for t
            4. loop through final array and return False if nonzero exists
        """
        if len(s) != len(t):
            return False
        
        count = [0 for i in range(26)]
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False
        return True   