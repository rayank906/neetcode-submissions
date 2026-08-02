class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] < -nums[k]:
                    j += 1
                elif nums[i] + nums[j] > -nums[k]:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
        return list(res)
        

"""
   0. res a set
   0b. sort input arr
   1. for every element in input arr
   2. perform a two sum operation to find the other two numbers
    a. l to idx + 1, r to last element
    b. if sum(nums[l], nums[r]) < -nums[idx]:
        l += 1
    c. if sum > -nums[idx], r -= 1
    d. else, add nums[i], j, k to res
    e. return list(res)

    TC: O(n^2), SC: O(n) 
"""
        