class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        occur = defaultdict(int)
        arr = [[] for i in range(len(nums) + 1)]
        for n in nums:
            occur[n] += 1
        for key in occur:
            arr[occur[key]].append(key)
        
        for i in reversed(arr):
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res

"""
    1. make a hash map with every unique element and its number of occurrences
    2. sort hash map in reverse order
    3. append first k elements to res list
    4. return res  
    TC:
        O(nlogn), n time for hashmap, nlogn time to sort, k time to choose k elements so nlogn dominates
    SC:
        O(n), n extra space for hashmap, k space for res

    //OPTIMIZE//
      1. make a hashmap of occurrences
      2. make list of lists of len(nums) where every index is the occurrences 
      3. loop through list in reverse order until you've appended k elements
"""
        