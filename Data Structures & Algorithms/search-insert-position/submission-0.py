class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return r + 1

"""
    binary search, return r
    1. set l, r to 0, len(nums) - 1
    2. calculate the mid
    3. if target > mid, reassign l to mid + 1
    4. if target < mid, reassign r to mid - 1
    5. else, element found, return mid
    6. repeat for all elements
    7. if loop exited, return r
"""
        