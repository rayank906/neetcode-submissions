class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
    
"""
    1. make ptrs to l and r. 
    2. while l <= r, calculate mid and compare mid value to targte
    3. if mid > target, send r to mid - 1
    4. if mid < target, send l to mid + 1
    5. else, value is found so return mid
    6. return -1 outside while loop
"""
        