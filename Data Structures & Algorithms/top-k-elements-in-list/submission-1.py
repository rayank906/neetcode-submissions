class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        occur = defaultdict(int)
        for n in nums:
            occur[n] += 1
        occur = dict(sorted(occur.items(), key=lambda item: item[1], reverse=True))
        i = 0
        for key in occur:
            res.append(key)
            i += 1
            if (i >= k): 
                break
        return res

"""
    1. make a hash map with every unique element and its number of occurrences
    2. loop through hash map, check every value against k
    3. append every val >= k to result list
    4. return result

    Edge cases:
        1. single element list, with k > 1
        2. no element had >=k instances    
"""
        