class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            1. make a set of nums, make a seen set
            2. init maxS = 0, currS = 0
            3. for every num in nums, if num not in seen
            4. while num + 1 in set
            5. currS += 1
            6. maxS = max(currS, maxS)
            7. return maxS
        """
        numSet = set(nums)
        seen = set()
        maxS, currS = 0, 0
        for num in nums:
            if num not in seen:
                temp = num
                seen.add(temp)
                currS += 1
                while temp + 1 in nums:
                    currS += 1
                    temp += 1
                    seen.add(temp)
                maxS = max(currS, maxS)
                currS = 0
        return maxS
        