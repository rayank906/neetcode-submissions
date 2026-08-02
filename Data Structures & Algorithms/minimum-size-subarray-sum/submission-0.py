class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = len(nums) + 1
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(r - l + 1, length)
                total -= nums[l]
                l += 1
        return 0 if length == len(nums) + 1 else length
                


"""
    1. set pointers to the start of the array
    2. set length to len(nums) + 1 (holds curr shortest subarray)
    3. set total to 0 (holds total of curr subarray)
    4. loop through nums, checking a window's total. while total >= target,
    shrink window by moving l forward.
    5. move r and recalculate window total
"""
        