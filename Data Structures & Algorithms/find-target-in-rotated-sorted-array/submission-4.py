class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            1. init l, r to 0, len(nums) - 1
            2. calc mid = l + r // 2
            3. while l <= r, 
            3b. if l < r
                if target > mid, l = mid + 1
                elif  t < mid, r = mid - 1
                else, return mid
            4. l > r, 
                a. mid > l, if target < mid and > l, r = mid
                            else, l = mid
                b. else, if target > mid and < r, l = mid
                            else, r = mid
            return -1
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
            
        