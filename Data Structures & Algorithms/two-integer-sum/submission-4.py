class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            1. loop through arr
            2. add to hashmap of idx as we visit
            3. as we loop, check if target - curr exist in hashmap
            4. once found, return map[diff], curr
        """
        valToIdx = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valToIdx:
                return [valToIdx[diff], i]
            valToIdx[nums[i]] = i
        
        