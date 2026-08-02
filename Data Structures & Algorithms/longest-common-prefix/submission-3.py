class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        pres = True
        for i in range(len(strs[0])):
            for s in strs:
                if i < len(s) and strs[0][i] == s[i]:
                    continue
                else:
                    pres = False
                    break
            if pres == False:
                return longest
            else:
                longest += strs[0][i]
        return longest
            
                


"""
    1. fl fs, loop through all char to see if they have it
    2. if they do, append it to longest pre
    3. repeat for all characters of first element
    4. return longest pre

    Edge cases:
        1. empty strings:
            if found, return ""
        2. all diff
            still has to do O(n) pass
"""
        