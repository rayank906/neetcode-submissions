# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if ((p.val < root.val and q.val > root.val) or 
            (p.val > root.val and q.val < root.val)):
            return root

        if (p.val == root.val) or (q.val == root.val):
            return root
        
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)


"""
    Case 1:
        p belongs right subtree
        q belongs left subtree
    p > root and q < root or opposite
    return root

    Case 2:
        p and q are in same subtree
        p and q are both less than root or opposite
        recursively call LCA

    TC: O(n)
    SC: O(h) where h is height of tree    
    
    Edge cases:
        if either is THE root node, return root
"""
        