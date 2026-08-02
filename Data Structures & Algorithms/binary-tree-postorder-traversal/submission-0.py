# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(root):
            if not root:
                return None

            traverse(root.left)
            traverse(root.right)
            res.append(root.val)
        
        traverse(root)
        
        return res
    
    """
        1. make a global res array
        2. make an inner traverse function to add elements recursively to the global array
        3. call the function on the root value
        4. return res
    """