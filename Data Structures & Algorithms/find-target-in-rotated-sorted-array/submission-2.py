class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

"""
   1. l, r to 0, len(nums) - 1
   2. calculate the mid
   3. if l <= mid, left sorted portion:
   4. if target < nums[mid] and target > nums[l]:
        r = mid - 1
        else, l = mid + 1
   5. if mid <= r, right sorted portion:
   6. if target <= r and > l:
        l = mid + 1
        else. r = mid - 1
   7. return -1

   TC: O(log n) divide search space in half
   SC: O(1) for a couple ptrs
"""
        