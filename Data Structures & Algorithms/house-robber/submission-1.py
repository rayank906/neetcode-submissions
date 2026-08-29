class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            - if 1 elem, return element
            - loop backwards from n-3 down
            - if i+2, i+3 are valid, choose max of both and incr
            - return max(arr[0], arr[1])
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        for i in range(n-3, -1, -1):
            if i == n-3:
                nums[i] += nums[n-1]
            else:
                nums[i] += max(nums[i + 3], nums[i + 2])
        return max(nums[0], nums[1])
