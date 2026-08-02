class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            1. init l, r to 0, len(nums) - 1
            2. init res to float inf
            3. while l < r, calc mid = l + r // 2
            4. if mid >= l, l = mid + 1
                b. if l < r, update res
            5. else, r = mid - 1
                b. if l < r, update res
            6. return res
        """
        l, r = 0, len(nums) - 1
        res = float("infinity")
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid
        return res
        
        

        