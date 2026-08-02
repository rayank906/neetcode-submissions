class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1
    
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                left = mid
                r = mid - 1
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                right = mid
                l = mid + 1
        
        return [left, right]

"""
   1. init left, right to -1 as return values
   2. perform one binary search for left
    a. if target found, save it as left value and search the left of mid again
    b. when loop ends, it will be leftmost value
   3. another one for right
    a. if target found, save it as right value and search right portion again
    b. when loop ends, it will be rightmost value
   
   TimeC: O(log n)
   SpaceC: O(1) 
"""