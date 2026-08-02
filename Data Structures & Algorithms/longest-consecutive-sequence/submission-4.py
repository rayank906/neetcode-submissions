class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        seq = {}
        ptr, trav = 0, 0
        seq[ptr] = 1
        while trav < len(nums) - 1:
            if (nums[trav] == nums[trav + 1]):
                trav += 1
                continue
            if abs(nums[trav] - nums[trav + 1]) == 1:
               seq[ptr] += 1
            else:
                ptr = trav + 1
                seq[ptr] = 1
            trav += 1
        res = 0
        for key, val in seq.items():
            if (val > res):
                res = val
        return res


"""
    1. sort
    2. make a idx: longest seq hashmap
    3. loop through sorted list. where a sequence breaks is
    where we start another
    [
        a. start at idx 0, check if next num is 1 greater. if it is, append dict
        b. if it isnt, make curr idx a new elem in dict init to 0, repeat process
        c. repeat until end of nums reached
    ]
    4. return longest value element of hashmap
"""



        