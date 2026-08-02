class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
            1. loop through nums
            2. add elements to set
            3. if seen, return true
            4. return false
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False