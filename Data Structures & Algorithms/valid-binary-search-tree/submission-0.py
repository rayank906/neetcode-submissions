# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.stack = []

        def dfs(root):
            if not root:
                return True
            
            left = dfs(root.left)
            if self.stack and self.stack[-1] >= root.val:
                return False
            else:
                self.stack.append(root.val)
            right = dfs(root.right)

            return left and right
        
        return dfs(root)

"""
    1. perform an inorder traversal on root
        left = traverse left
        if stack and stack[-1] >= root.val:
            return False
        right = traverse right
        return left and right

    TimeC: O(n), traversal of every node
    SpaceC: O(n), a stack for extra memory
"""
        