# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def height(root):
            if not root:
                return 0
        
            left = height(root.left)
            right = height(root.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        height(root)
        return self.res
        

"""
    1. calculate diameter by summing l and r
    2. update global res accordingly
    3. height = max(l, r) + 1
    4. diameter = height(l) and height(r)
    5. return res

    TC: O(n)
    SC: O(n) for the call stack
"""
        