# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                smallest = self.minNode(root.right)
                root.val = smallest.val
                root.right = self.deleteNode(root.right, smallest.val)
        return root

"""
    Helper [MinNode]:
        while root.left:
            minNode = root.left
        return minNode
    
    Base case:
        if null root, return None
    1st case, 0 or 1 child:
        return the valid child
    2nd case, 2 children:
        find minNode in right subtree
        replace node value with minNode value
        delete minNode from tree
    return root
"""
        