class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            1. for every elem
            2. loop through all elems
            3. if i + j == target, return i, j
        """
        for i in range(len(nums)):
            for j in range(i +  1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        