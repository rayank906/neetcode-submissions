class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            mid = (l + ((r - l) // 2))
            minimum = min(minimum, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minimum

"""
    1. set l, r to 0 and len(nums) - 1
        make a min variable
    2. calculate mid
    3. assign min to mid
    3b. if l < r, [range is sorted so take leftmost], min = min(min, l)
    4. if mid >= l, r = mid - 1
    5. else, l = mid + 1
    6. return min
"""
        