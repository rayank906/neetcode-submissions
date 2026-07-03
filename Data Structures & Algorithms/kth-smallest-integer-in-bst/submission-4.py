# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
            1. define a res array
            2. define a inorder helper
                a. if not root, return
                b. traverse left
                c. add root.val to array
                d. traverse right
            3. call inorder helper
            4. return res[k - 1] for 0 index
        """
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res[k - 1]
        