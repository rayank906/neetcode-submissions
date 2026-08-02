# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            return (root.val == subroot.val) and sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right)
        
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return True
        
        if root.val == subRoot.val:
            isSameTree = sameTree(root, subRoot)
            if isSameTree:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

"""
    1. Base cases: if root null, return True
        if root or subroot null and other not null, return False
    2. For every node, compare if they are the same trees
    3. Use a helper function isSametree to compare the nodes
    4. for every node, check isSameTree on nodes with same value as subRoot
    5. if isSame returns false, try again recursively
    6. if isSame returns true, return the node

    TC: O(n * s) where n is root and s is subroot
    For every node, we're going through s nodes to check for isSameTree

    SC: O(n * s) for recursive call stack
    For every node, we are creating s stack frames when calling isSameTree
"""

        