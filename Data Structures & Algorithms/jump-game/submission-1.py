class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            - goal = last idx
            - from n-2, if it can reach goal update goal
            - repeat until goal == 0
        """
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        