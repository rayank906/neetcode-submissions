# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
            1. make a same tree helper
            2. base cases
                a. if not subroot, return true
                b. if not root, return false
                a. if same tree, return true
                b. return subtree(root.left, sub) or subtree(root.right, sub)
            3. sameTree()
                if both null, return true
                if one null, return false
                if val not equal, return false
                return sametree(left, left) and sameTree(right, right)
        """
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        