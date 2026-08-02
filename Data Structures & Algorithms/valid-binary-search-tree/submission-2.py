# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
           1. perform inorder traversal
           2. while adding to array,
                if curr < last arr elem, return False
           3. if arr successfully built, return True 
        """
        res = []
        def inorder(root):
            if not root:
                return True
            left = inorder(root.left)
            if res and res[-1] >= root.val:
                return False
            res.append(root.val)
            right = inorder(root.right)
            return left and right
        return inorder(root)
