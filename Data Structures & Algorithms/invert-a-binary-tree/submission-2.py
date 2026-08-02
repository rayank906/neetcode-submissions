# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            1. base case: if not root, return none
            2. assign root.left to inverted right tree
            3. assign root.right to inverted left tree
        """
        if not root:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root
        