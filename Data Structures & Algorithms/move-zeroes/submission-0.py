class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = []
        count = 0
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                count += 1
        for i in range(count):
            res.append(0)
        for i in range(len(nums)):
            nums[i] = res[i]
        
        