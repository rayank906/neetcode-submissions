# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
    Base cases:
    a. p and q null, return True
    b. p null and q or p and q null, return False
    c. return (p.val == q.val) and 
    isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
"""
        