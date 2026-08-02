class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            1. make a set of nums, make a seen set
            2. init maxS = 0, currS = 0
            3. for every num in nums, if num - 1 not in nums, start of a sequence
            4. while num + 1 in set
            5. currS += 1
            6. maxS = max(currS, maxS)
            7. return maxS
        """
        numSet = set(nums)
        maxS, currS = 0, 0
        for num in nums:
            if num - 1 not in nums:
                temp = num
                currS += 1
                while temp + 1 in nums:
                    currS += 1
                    temp += 1
                maxS = max(currS, maxS)
                currS = 0
        return maxS
        