class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for h in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[h] == target:
                            res.add((nums[i], nums[j], nums[k], nums[h]))
        return list(res)

"""
    brute force:
    TC: O(n^4), SC: O(1)

    1. for every element,
    2. for every second element,
    3. for every third element,
    4. check every fourth element and see if the sum == target
    5. if it does, add it to result list
    6. return res list
"""
        