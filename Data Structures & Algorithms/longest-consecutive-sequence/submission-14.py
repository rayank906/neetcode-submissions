class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            - set of elems
            - if num - 1 there, next
            - if not, its start of seq
            - build seq by checking if in set
            - update longest
            - return longest
        """
        longest = 0
        numSet = set(nums)
        for n in nums:
            curr = 1
            if n - 1 in numSet:
                continue
            else:
                while n + 1 in numSet:
                    curr += 1
                    n += 1
                longest = max(curr, longest)
        return longest      