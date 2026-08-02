class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1

"""
    Use bucket sort
    1. create an array and pass once to count occurrences of each
    2. Use a second pass to populate array with acquired counts
"""
        