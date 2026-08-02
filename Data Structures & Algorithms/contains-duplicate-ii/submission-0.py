class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        window.add(nums[l])
        for r in range(1, len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False


"""
    fixed size sliding window
    1. hashSet for window
    2. l = 0, for every r, check if nums[l] == nums[r]
    3. as soon as r - l >= k, remove nums[l] from hashSet and l += 1
    4. add nums[r] to window
    5. return false outside

    Edge cases:
        Equal numbers in the last window
"""
        