class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            1. make occurences array with len(nums)
            2. build freqMap
            3. populate occurences array using freqMap
            4. loop through occurrences arr backwards
            5. fetch and return top k elements
        """
        occur = [[] for i in range(len(nums) + 1)]
        res = []
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1
        for key, value in freqMap.items():
            occur[value].append(key)
        for i in range(len(occur) - 1, -1, -1):
            for j in occur[i]:
                if len(res) == k:
                    return res
                res.append(j)
        return res