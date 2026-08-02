# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth_l, depth_r = 1, 1
        depth_r += self.maxDepth(root.right)
        depth_l += self.maxDepth(root.left)
        return max(depth_l, depth_r)
        

"""
    1. for every node, calc depth l and r and return max
    2. base cases, not root, return 0
    3. init depth l and depth r to 1
    4. calculate depth of left and right subtree and return max

    TC: O(n) traversing all the nodes to calculate depth
    SC: O(n) for the recursive call stack
"""
        