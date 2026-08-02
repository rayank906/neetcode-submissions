class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
            1. make hashmap mapping from s and t and t to s
            2. check s to t map and t to s map to ensure mapping works
                a. if not in s and not in t, map
                b. if not in s but t in t map, return false
                c. if match, ignore
                d. else return false
        """

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if s[i] not in s_to_t:
                if t[i] not in t_to_s:
                    s_to_t[s[i]] = t[i]
                    t_to_s[t[i]] = s[i]
                else:
                    return False 
            elif s_to_t[s[i]] == t[i] and t_to_s[t[i]] == s[i]:
                continue
            else:
                return False
        return True
        
        