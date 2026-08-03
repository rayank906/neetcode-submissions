class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            1. two ptrs at beg and end
            Cases:
                mid > l, < r: sorted normally
                mid > l, > r: left sorted portion
                mid < l, < r: right sorted portion
                mid < l, > r: 
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] < nums[r]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    return mid
            else:
                if nums[mid] == target:
                    return mid
                if nums[mid] >= nums[l]:
                    if target <= nums[mid] and target >= nums[l]:
                        r = mid
                    else:
                        l = mid + 1
                else:
                    if target >= nums[mid] and target <= nums[r]:
                        l = mid
                    else:
                        r = mid - 1
        return -1

        