from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            0. for every elem
            1. build a count arr of 26 chars (a - z)
            2. add elem to count to val hashmap using count arr
            3. return values in hashmap

            Time: O(n * m)
            Space: O(n)
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        