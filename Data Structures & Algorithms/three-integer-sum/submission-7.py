class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            1. sort the input array
            2. for every num, search for two nums that sum to -num
            3. init l, r to i + 1 and len(nums) - 1
            4. while l < r,
                if total < target, l += 1
                if total > target, r -= 1
                else add sum to output and keep searching
            4. after loop, move i until nums[i] is different

            [We never want elems in same position after we've found a sol
            so we move for dupes after every instance of a solution found]
        """
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            target = -(nums[i])
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
            skip = nums[i]
            while i < len(nums) and nums[i] == skip:
                i += 1
        return res
        