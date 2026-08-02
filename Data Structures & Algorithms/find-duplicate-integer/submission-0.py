class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        
        return slow


"""
    The array elements are in range [1, n]
    This means we can represent it as a linked list
    of their indexes and they point to the value in range [1, n]
    that they hold
    since two or more elements have the same value, there must
    exist a cycle somewhere
    
    1. use a fast and slow pointer approach to loop through array
    [use mod to enable cycling]
    2. when they meet, create another slow pointer
    3. move both slow pointers until they meet
    4. by Floyds T&H, they are guaranteed to meet at the beginning of the cycle
    which in this case represents the duplicate index

    TC: O(n) for two passes SC: O(1) only a couple ptrs made
"""
        