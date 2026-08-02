class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1
        
        occur = [[] for i in range(len(nums) + 1)]
        for key in freq:
            occur[freq[key]].append(key)
        
        for i in range(len(occur) - 1, -1, -1):
            for j in occur[i]:
                res.append(j)
                if len(res) == k:
                    return res

"""
    1. make a freq map
    2. make an array of lists of length of nums + 1
        this array's indexes represent the number of occurrences
    3. after making freq map, loop through it and populate array of lists
    4. loop through array of lists and append k elements to res
    5. return res

    TimeC: O(n), n pass for freq map, n pass for populating array, k pass for pop. res
    SpaceC: O(n), n for freq map, k for res array
"""
        