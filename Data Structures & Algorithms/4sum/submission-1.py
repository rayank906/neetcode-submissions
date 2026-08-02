class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] + nums[j] < target:
                        l += 1
                    elif nums[l] + nums[r] + nums[i] + nums[j] > target:
                        r -= 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
        return list(res)

"""
    two sum on last 2 numbers:
    TC: O(n^3), SC: O(n)

    1. make a res set
    1b. sort the input arr
    2. for every element,
    3. for every second element
    4. perform two sum to find last 2 elements needed for sum
        a. l, r set to j + 1, len(nums) - 1
        b. if sum < target, l += 1
        c. if sum > target, r -= 1
        d. else, add nums[i], nums[j], nums[l], nums[r] to res set
    5. return list(res)
"""
        