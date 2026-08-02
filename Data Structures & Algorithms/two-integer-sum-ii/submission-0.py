class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]

"""
    2ptr
        1. init l, r ptrs at beginning
        2. sum and comp to target
            i. if greater, r--
            ii. if less, l++
        3. since there is a solution, return l and r ptrs
"""
        