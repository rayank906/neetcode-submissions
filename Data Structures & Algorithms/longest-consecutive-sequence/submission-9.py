class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        lcs = 0

        for num in nums:
            if (num - 1) not in nums_set:
                count = 1
                while (num + count) in nums_set:
                    count += 1
                lcs = max(lcs, count)
        return lcs

"""
    1. make a hashset of elements
    2. for every element in the hash set, only start a sequence if its
    -1 element doesn't exist
    3. make a count variable
    4. while, num + 1 in set, count += 1
    5. lcs = max(lcs, count)
    6. return lcs

    TimeC: O(n), loop through array once
    SpaceC: O(n) for the extra hashset
"""